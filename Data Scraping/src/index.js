const { fetchProfileSuggestedAccounts } = require('./modules/fetchProfileSuggestedAccounts');
const { fetchProfileData } = require('./modules/fetchProfileData');
const InstagramData = require('./lib');
//const { profile } = require('console');

async function scrapeInstagramData() {
    const workDir = __dirname + "\\data\\"
    const api = new InstagramData({ username: '*******', password: '*******'})	//substitute username and password

    console.log("Login to Instagram..")

    let res = await api.logIn()
    if(res) {
        console.log("Login success")
    }
    else {
        console.error("Login failed...exiting")
        return
    }

    await fetchProfileSuggestedAccounts(api, workDir)
    await fetchProfileData(api, workDir)
}

console.log("Instagram data scraping...")
scrapeInstagramData()











