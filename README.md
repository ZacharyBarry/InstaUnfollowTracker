# **How to Use the Instagram Unfollower Application**

This application allows you to identify Instagram profiles that you follow but who are not following you back. Follow the steps below to download your Instagram data and use this app.

## **Step 1: Download Your Instagram Data**
To compare your followers and following lists, you first need to download your Instagram data in the form of a `.zip` file containing JSON files.

1. **Open Instagram on your browser:**
   - Go to [Instagram.com](https://www.instagram.com) and log in to your account.

2. **Request your data:**
   - Click on your profile picture in the top-right corner and go to **Settings**.
   - In the **Privacy and Security** section, scroll down to **Data Download**.
   - Click **Request Download**.
   - Select **JSON** as the format.
   - Enter your email address and password when prompted, then click **Next**.
   - Instagram will send you an email with a link to download your data. This may take some time.

3. **Download the `.zip` file:**
   - Once you receive the email, click the download link.
   - Save the `.zip` file to your computer and extract its contents. You will find a folder containing various JSON files. The files we need are:
     - `followers_and_following/followers.json`
     - `followers_and_following/following.json`

## **Step 2: Upload Your Data to the Application**
Now that you have the data, you can use the Instagram unfollower application by manually uploading the JSON files.

1. **Open the application:**
   - Launch the application by running the Python script.

2. **Upload the required files:**
   - You will be prompted to upload two files:
     - `followers.json` (lists your followers)
     - `following.json` (lists the profiles you are following)
   - Use the "Upload" buttons in the app interface to select these files from your computer.

3. **Start the process:**
   - The app will process the data and generate a list of profiles that you follow but who are not following you back.

## **Step 3: View the Results**
- The results will be put into a list of usernames where you can click on the name and be transported directly to the Instagram account.
- Once a name is clicked on, the name will be popped off the list.

---

### **Additional Notes:**
- Make sure to request a fresh copy of your Instagram data regularly to keep your information up to date.
- This app works by uploading the files manually, so it doesn’t connect directly to Instagram’s servers or API.
