const { writeToFile, writeArrayToFile, readArrayFromFile } = require('../util/writeToFile');
require('dotenv').config();
const { setTimeout } = require('timers/promises');
var fs  = require('fs');
const util = require('util');
const sleep = util.promisify(setTimeout);

async function scrape(api, workDir, inputUserNames, processedUserNames, errorUserNames) {
    console.log("Start scraping ")
    let i = 0;
    let count = 0;
    for(; i < inputUserNames.length; ++i)
    {
        let userName = inputUserNames[i].trim()
        userName = userName.replace('\r', '')
        if( (userName.length == 0) || (processedUserNames.includes(userName)) )
        {
            console.log("Ignoring username: ", userName)
            continue
        }
        
        console.log("Processing username: ", userName)
        let userAccountData = {}
        try {
            let userSharedData = await api.fetchProfileSharedData(userName)
            if(userSharedData == null) {
                console.error("No Shared data received for user: ", userName)
                errorUserNames.push(userName)   
                break                     
            } 
            else 
            {
                userAccountData.profile = userSharedData.profileInfo  
                
                let mediaData =  await api.fetchMediaData(userSharedData.mediaInfo)
                if( (mediaData.length > 0) && ('comments' in mediaData[0]) )
                {
                    userAccountData.media = mediaData
                }                    
                else {
                    console.error("No comments/media received")
                    errorUserNames.push(userName)
                    break    
                }                    

                processedUserNames.push(userName)
                writeToFile(userAccountData, workDir +  userName + '.json')                
                count = count + 1
                let sleepDuration
                if(count % 50 == 0) {
                    sleepDuration =  3600000
                }
                else if(count % 10 == 0) {
                    sleepDuration =  1800000
                } else {
                    sleepDuration =  5000
                }                     
                console.log("Going to sleep for: ", sleepDuration)
                await sleep(sleepDuration)                    
            } 
                
        } catch(error) {
            console.error("Error processing username: ", userName, error)
            errorUserNames.push(userName)                        
        }
    }  

    console.log("Done processing usernames.")   

    if(errorUserNames.length > 0) {
        console.log("Persisting error usernames")
        writeArrayToFile(errorUserNames, workDir + 'error.txt')
    }

    if(processedUserNames.length > 0) {
        console.log("Persisting processed usernames")
        writeArrayToFile(processedUserNames, workDir + 'processed.txt')
    }

    if( i < inputUserNames.length) {
        console.log("Persisting left over input usernames")
        writeArrayToFile(inputUserNames.slice(i, inputUserNames.length), workDir + 'suggested_accounts.txt')
    }
    else if(i == inputUserNames.length) {
        console.log("Processed all inputs")
        writeArrayToFile([], workDir + 'input.txt')
    }    
}


async function fetchProfileData(api, workDir) {
    console.log("Fetch profile data")
    var inputUserNames = []
    var errorUserNames = []
    var processedUserNames = []
    try {
        inputUserNames =  readArrayFromFile(workDir + 'suggested_accounts.txt')
        processedUserNames =  readArrayFromFile(workDir + 'processed.txt')
        errorUserNames =  readArrayFromFile(workDir + 'error.txt')
        console.log(inputUserNames)
    } catch(error) {
        console.error("Error reading input files: ", error)
        return
    }

    if(inputUserNames.length == 0) {
        console.log("No profile specified to fetch data")
        return
    }

    scrape(api, workDir, inputUserNames, processedUserNames, errorUserNames)
}

module.exports = {
    fetchProfileData
}