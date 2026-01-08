# Logic Design: User Authentication Component (Initial Draft)

## 📌 Project Context
This document represents the **original logical blueprint** for the login module of the "Gelos Enterprises" project. 

> **Developer Note:**
> The final implementation in the source code has evolved from this initial version. You can view the complete, refined code here: 
> 🔗 **[Final Implementation: Gelos Enterprises System](https://github.com/Tina-YingWang-AU/User-Auth-System-Python)**
>
> I have preserved this original draft here to document my starting point and logic-building process during the Certificate III course.

---

### 📝 Original Pseudocode Implementation

```plaintext
Pseudocode for Component 2: Checking a username and password (Logging in)
 
BEGIN
     DECLARE checkLogin = FALSE
     DECLARE maximumAttempts = 3      
 
     // Main loop for login attempts
     LOOP for maximumAttempts Times
         SET checkLogin = FALSE
         
         // Loop to validate username input to make sure it is not empty
         WHILE TRUE
             ASK user for UName
             IF the trimmed and lowercased version of UName is empty THEN
                  DISPLAY Error message
             ELSE
                  EXIT LOOP // Exit the username validation loop
             END IF
         END WHILE 
     
         ASK user for PWord
 
         // Open and read "accounts.txt" text file
         OPEN the "accounts.txt" file in READ Mode
         
         // Exception handling - file-related errors
         IF file cannot be accessed THEN
              DISPLAY Error message
              END PROGRAM
         ELSE
 
              // Loop to check each line in the file for matching credentials
              LOOP through each line in the file
                  READ One Line from file INTO LineRecord
                  SPLIT LineRecord INTO list of Fields using the comma as a separator
                  
                  IF the list of Fields is not empty THEN
                      EXTRACT the stored username and password from the list of Fields
                      TRIM spaces and CONVERT stored username to lowercase
                      TRIM spaces and CONVERT UName to lowercase
              
                      // Check for match
                      IF UName = stored username AND PWord = stored password THEN
                           SET checkLogin to TRUE
                           EXIT LOOP // Exit file reading loop
                      END IF
                  END IF
              END LOOP // End the file reading loop
 
              CLOSE "accounts.txt"
         END IF
 
         // Process login result
         IF checkLogin = TRUE THEN
              DISPLAY Login Successful message
              EXIT LOOP // Exit the main loop for login attempts
         ELSE
              DISPLAY Login Fail message with current attempt count
 
              // Check if maximum number of consecutive failed attempts reached
              IF this is the final allowed attempt THEN
                   DISPLAY Maximum Attempts reached and Account Locked message
              ELSE
                   // Ask user if they want to try logging in again
                   // Loop to validate user input to continue
                   WHILE TRUE
                        ASK user if they want to try logging in again [y/n]
                        IF lowercased version of response is not "y" and is not "n" THEN
                            DISPLAY Error message 
                        ELSE
                            EXIT LOOP // Exit the user input validation loop
                        END IF
                   END WHILE // End the user input validation loop
 
                   // Process user's choice to continue or not
                   IF user chose "y" THEN
                        DISPLAY Continue to next attempt message
                        // Main loop for login attempts will continue naturally
                   ELSE
                        DISPLAY Exit message
                        EXIT LOOP // Exit the main loop for login attempts
                   END IF
              END IF
         END IF
 
     END LOOP // End the main loop for login attempts
 
END
