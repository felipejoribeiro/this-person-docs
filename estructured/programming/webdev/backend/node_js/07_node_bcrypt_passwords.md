# Bcrypt.js package for password encryption
When we are dealing with user passwords and sensitive information we have to avoid saving such data without safety. One method for that is by encrypting the information. We can store the password like bcrypt hashes.

The packages you can use are `bcrypt` and `bcrypt.js`. The first is the oldest and more frequently maintained and has two dependencies, and the second has no dependencies and was created in plain javascript. Both are used in production being the second more frequently downloaded. They can be installed with:

- `npm i -S bcrypt` to install and `npm r -S bcrypt` to remove.
- `npm i -S bcryptjs` to install and `npm r -S bcryptjs` to remove.

On this text we will use the `bcrypt-nodejs` that is a deprecated package. Don't use it for production, but the principles are the same. This was used in the tutorial because it is compatible with mac and windows, but it's fairly simple to convert afterwords to a better package.

With this tool we can store passwords not as plain text, but as hashes. After installing `bcrypt-nodejs` with *npm* you can insert the following in your server javascript file:

```javascript
const bcrypt = require('bcrypt-nodejs');

bcrypt.hash("bacon", null, null, function(err, hash) {
  // Store hash in your password DB.
});

// Load hash from your password DB.
bcrypt.compare("bacon", hash, function(err, res) {
    // res == true
});
```

The first function is used to create hashes in your database. That is, it encrypt the given information. The second function compares a text with a given hash, so that if the text is the same with the one that originated the hash it returns `true`.

It's important to know that those functions are asynchronous.

About information security, it is important to always use the `https` protocol to communicate with a cliente. This is important as even if the client send plain text passwords to compare with the hash. Here goes an article about information security applyied to web development by Andrew:

## Andrew's take on information security for authentication

This tutorial will cover the user experience from the front end, all the way to the database. Let’s get started.

### Step 1:
- It all begins when you ask your user to create an account by setting a username and password. This is where user experience will need to play nicely with proper security measures. United States National Institute for Standards and Technology (NIST) is currently finalizing their recommendations for password management. Some of these include:

- Your minimum password length should be at least 8 characters, and the maximum as large are 64 characters for the user. The longer the password that the user sets, the better. This will also play nicely if said user is using password managers like 1Password since their generated password will be long and fit this criteria. There is nothing worse than the password limit being too small for a password generated by 1Password.

- Do accept both ASCII and UNICODE characters and don't set rules about which characters should and shouldn’t be included (P@ssword1 is NOT a good password). Instead, encourage people to set long passwords with high entropy (upper case letters, lower case letters, digits, special characters).

- Don’t allow password hints.

- Avoid security questions. Although this is good for an extra layer of security, the information can be easily discovered by an attacker in this day and age. It’s just an extra implementation step; a step that a user has to take while offering very little added security. Yahoo had this information stolen-- which was saved in plain text, allowing the attacker to easily see this information about each user.

- Use 2FA (2 factor authentication) if you want an extra layer of security in your application, but avoid using SMS as this can be easily hacked to have the attackers phone receive the confirmation code.

- Once the user has registered, there are two things to keep in mind:

  - Don’t let the user know the password was incorrect when logging in. Instead, mention that the username and password combination is incorrect. You want to minimize information that an attacker can get, and the less they know (such as that the user exists), the better.

  - The only time passwords should be reset by an administrator is when they suspect that an account has been compromised. Otherwise, passwords should only be reset by a user when he or she has forgotten their credentials.

### Step 2:
Now that the user has entered a good password, they will submit the form and trust you to take care of their credentials. In the second step, you are transmitting the form (account sign up) data in a POST body to your server. You do it this way for a few reasons:

- POST requests are never cached
- POST request will not remain in the browser history
- No restriction on data length

Most importantly, use HTTPS so that this data will be encrypted and cannot be attacked by someone who is observing your network traffic. HTTPS is the regular HTTP protocol with SSL/TLS encryption which means that only the server can read what you send it, and only you can read what the server sends back. To use HTTPS, simply purchase an SSL certificate and follow the steps in this article.

### Step 3:
Now that we have received the username and password to our server it is time to do a few things. Before we get started though, always remember to never store passwords in plaintext. Instead, you will want to use some of these popular npm packages to hash the password: argon2, scrypt, or bcrypt. We prefer bcrypt for three reasons:
1. bcrypt is 15 years old and has been vetted by the crypto community. Although argon2 won last year’s password hashing competition, it is still fairly new and we would like to see it have a longer lifespan in the crypto community.
2. scrypt is 7 years old and also a good choice, but bcrypt is a bit easier to implement in a node.js server with simpler documentation as you will see below in the example.
3. The bcrypt npm package is better over other bcrypt implementations available on npm since it is native, highly popular, and vetted by the community without trying to reinvent the wheel.

Now you might be asking yourself, why not just use a hashing function like SHA256, add a salt (randomly generated bytes to place in front of the password) for each user, and store those in a database? The problem with computing power increasing is that attackers can now use GPUs to try out passwords at over 100 million per second and see if they get a hit. That’s why you want to use hash functions that were specifically designed to be slow. Although it is fast enough so the user won’t notice (about 100ms), it is long enough to make it infeasible for an attacker to try out a long list of passwords. bcrypt allows you to add a saltRound (10 is the recommended value) which iterates 2^10, or 1024 times over the password in a process called key stretching. Finally, bcrypt implementation is also safe from timing attacks. Here is a simple overview of how to use bcrypt for password management. (you can check out their repo for more detail):

```javascript
import bcrypt from'bcrypt'
const saltRounds = 10 // increase this if you want more iterations  
const userPassword = 'supersecretpassword'  
const randomPassword = 'fakepassword'
 
const storeUserPassword = (password, salt) =>  
  bcrypt.hash(password, salt).then(storeHashInDatabase)
 
const storeHashInDatabase = (hash) => {  
   // Store the hash in your password DB
   return hash // For now we are returning the hash for testing at the bottom
}
 
// Returns true if user password is correct, returns false otherwise
const checkUserPassword = (enteredPassword, storedPasswordHash) =>  
  bcrypt.compare(enteredPassword, storedPasswordHash)
 
 
// This is for demonstration purposes only.
storeUserPassword(userPassword, saltRounds)  
  .then(hash =>
    // change param userPassword to randomPassword to get false
    checkUserPassword(userPassword, hash)
  )
  .then(console.log)
  .catch(console.error)
```

That’s it! You can now rest assured that you have stored the user password securely. The interesting thing with security is that it is always a cat and mouse game. Security advice changes with the time as new exploits are discovered and computing power increases. New attacks will be discovered but so will new solutions. Remember, the best security for your application means constantly keeping up with vulnerabilities, software updates, and new tools. For now, you can breathe easy…
