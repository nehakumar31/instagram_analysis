const Instagram = require('instagram-web-api');
const { writeToFile, writeTextToFile } = require('../util/writeToFile');
require('dotenv').config();

class InstagramData {
    constructor(
        { username, password }
      ) {
        this.client = new Instagram({ username:username, password:password});   // add username and password
      }

    async fetchProfileChainData(userId) {
        console.log("Searching for userID =>", userId);
        try {
            const profile = await this.client.getChainsData({ userId });
            return profile;
            // return profile.slice(0, 2);   // splice(0, number of profiles to fetch in each)
        } catch (error) {
            console.log(error);
        }
    }

    async logIn() {
        console.log("Login.....")
        try{
            const loginResp = await this.client.login();            
            console.log("Login Response content: ", loginResp)        
            if ( ('authenticated' in loginResp) && (loginResp['authenticated']) ){
                return true  
            }
        } catch(err) {
            console.log(err)
            if(err.error && err.error.message == 'checkpoint_required') {
                let challengeUrl = err.error.checkpoint_url;
                console.log("Challenge url: ", challengeUrl)
                challengeUrl = '/challenge/?next=/'
                let challengeResp = await this.client.getChallenge({ challengeUrl:challengeUrl})
                console.log("Challenge res: ", challengeResp)
                const test = await this.client.updateChallenge({ challengeUrl, choice: 1});
                const code = reader.question('Insert Code: ');
                await rhis.client.updateChallenge({challengeUrl, securityCode: code});
            }
        }
        try {
            await this.client.login()
        } catch(err) {
            console.error("Login didn't suceed even after update challenge")
        }
    
        return false
    }

    async fetchProfileSharedData(userName) {
        console.log("Fetch profile shared data for userName: ", userName)
        try {
            let sharedInfo = await this.client.getUserByUsername({username:userName})
            if(sharedInfo == null){
                console.error("No data received")
                return
            } 
    
            let profileInfo = {
                biography : sharedInfo['biography'],
                username : sharedInfo['username'],
                followers_count: sharedInfo['edge_followed_by']['count'],
                following_count: sharedInfo['edge_follow']['count'],
                full_name: sharedInfo['full_name'],
                id: sharedInfo['id'],
                is_business_account: sharedInfo['is_business_account'],
                is_joined_recently: sharedInfo['is_joined_recently'],
                is_private: sharedInfo['is_private'],
                posts_count: sharedInfo['edge_owner_to_timeline_media']['count'],
                profile_pic_url: sharedInfo['profile_pic_url'],
                external_url: sharedInfo['external_url'],
                business_email: sharedInfo['business_email'],
                business_phone_number: sharedInfo['business_phone_number'],
                business_category_name: sharedInfo['business_category_name'],
                website : sharedInfo['business_address_json'],
                overall_category_name : sharedInfo['overall_category_name'],
                category_enum : sharedInfo['category_enum'],
                category_name : sharedInfo['category_name'],
                connected_fb_page : sharedInfo['connected_fb_page'],
                pronouns : sharedInfo['pronouns'],
                is_verified : sharedInfo['is_verified']
            }
    
            let mediaInfo = []
            if ('edge_owner_to_timeline_media' in sharedInfo)
            {
                mediaInfo.push(...sharedInfo['edge_owner_to_timeline_media']['edges'])
            }
    
            return {profileInfo, mediaInfo} 
    
        } catch(error) {
                console.log(error)
        }
    
        return         
    }

    async fetchComments(mediaShortCode) {
        console.log("fetch comments for media: ", mediaShortCode)
        try {
            let commentsResponse = await this.client.getMediaComments({shortcode: mediaShortCode,first:20})
            console.log("Number of comments received: ", commentsResponse.count)
            return commentsResponse.edges
        } catch(error) {
            console.error("Error fetcing comments for media: ", mediaShortCode, error)
        }    
    }
    
    async fetchMediaDetails(mediaItem) {
        if(mediaItem == null) {
            console.error("Null media item, nothing to process")
            return;
        }
    
        let mediaShortCode = mediaItem.shortcode
        console.log("Fetch media details for media id: ", mediaShortCode)
    
        let mediaDetails = mediaItem
        let comments = await this.fetchComments(mediaShortCode)
        if(comments != null) {
            mediaDetails.comments = comments
        }   
        
        return mediaDetails
    }

    async fetchMediaData(mediaInfo) {
        console.log("Fetch media and comment details from shared media info...")
        if(mediaInfo == null) {
            console.error("No media info to fetch details from")
            return;
        }
    
        if(mediaInfo.length == 0) {
            console.error("No media posts of user")
            return;
        }
    
        let mediaData = []
        let maxIter = Math.min(10, mediaInfo.length)
        for(let i =0; i < maxIter; ++i) 
        {
            let mediaPayload = mediaInfo[i]['node']
            let mediaDetails = await this.fetchMediaDetails(mediaPayload)
            mediaData.push(mediaDetails)
        }
    
        console.log("Received details on media items: ", mediaData.length)
        return mediaData    
    }

    async logOut(){
        console.log("Log out..")
        try {
            const logoutResponse = await this.client.logout()           
            return true
        } catch(error) {
            console.error("Error while logging out: ", error)
        }
    
        return false
    }
}

module.exports = InstagramData
