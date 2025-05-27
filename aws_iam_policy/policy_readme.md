Questions for the Json files are:

1. Create an IAM user and attach a custom policy that satisfy the below condition
The user should only have access to see the list of files on any bucket name that has the word spark-job in s3. 
Please you need to use pattern matching to match the buckets with the word spark-job
However, The user should be able to delete any file in the bucket spark-job-data-input in the folder dumps except for the files that ends with csv.
Please use pattern matching to exclude the csv.

2. Using the same user created in create_user, create another custom-policy that will allow the user to only 
 Create an IAM user if the word engineer starts it. Basically if the user creates a user called daniel for example, the user should get permission denied, but when the user creates the user like this engineer_daniel, it should be created.


