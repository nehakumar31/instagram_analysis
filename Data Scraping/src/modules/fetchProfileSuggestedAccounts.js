const { getUniqueObjects } = require('../util/getUniqueObject');
const { writeToFile, readArrayFromFile, writeArrayToFile } = require('../util/writeToFile');
var fs  = require('fs');
//require('dotenv').config();
const util = require('util');
const sleep = util.promisify(setTimeout);

async function getProfilesForAProfile(api, profile) {
    let profileList = [];
    try {
        let nextProfileList = await api.fetchProfileChainData(profile.id);
        profileList = nextProfileList;
    } catch (error) {
        console.error(error);
    }
    return profileList;
}

async function subsequentProfiles(api, workDir, allProfiles, level) {
    let nextProfiles = allProfiles, totalProfiles = allProfiles;    
    try {
        for (let temp = 0; temp < level; temp++) {
            let nextProfileList = [];
            for (let j = 0; j < nextProfiles.length; j++) {
                let data = await getProfilesForAProfile(api, nextProfiles[j]);
                nextProfileList.push(...data);
                await sleep(5000)                
            }
            
            let uniqueProfileList = getUniqueObjects(nextProfileList);            
            totalProfiles.push(...uniqueProfileList);
            console.log("Length of totalProfiles after append: %d", totalProfiles.length)
            nextProfiles = uniqueProfileList;
        }

        uniqueTotalProfiles = getUniqueObjects(totalProfiles);
        console.log("Length of uniquetotalProfiles: %d", uniqueTotalProfiles.length)
        const UsernamesList = uniqueTotalProfiles.map(obj => obj.username);
        console.log(UsernamesList)        
        writeArrayToFile(UsernamesList, workDir + 'suggested_accounts.txt');        
    } catch (error) {
        console.error(error);
        return false
    }

    return true
}

async function fetchProfileSuggestedAccounts(api, workDir){
    console.log("Fetch profile suggested accounts...")
    try {
        var initialAccounts =  readArrayFromFile(workDir + 'initial_userids.txt')        
    } catch(error) {
        console.error("Error reading input file: ", error)
        return
    }
    console.log("Initial accounts: ", initialAccounts)
    let firstLevelProfilesList = []
    for (let i = 0; i < initialAccounts.length; i++) {        
        let profiles = await api.fetchProfileChainData(initialAccounts[i]);           
        firstLevelProfilesList.push(...profiles)
    }
    
    try {
        await subsequentProfiles(api, workDir, firstLevelProfilesList, 1);  //(allProfiles, depth of profiles needed)
    } catch (error) {
        console.error(error);
    }     
}

module.exports = {
    fetchProfileSuggestedAccounts
}
