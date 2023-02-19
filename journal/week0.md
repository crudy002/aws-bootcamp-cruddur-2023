# Week 0 — Billing and Architecture
TO-DO Pre Week 0
---------------
- [x] Created new gmail to support new aws account: cruedigertech@gmail.com
- [x] Created GitHub repository from template repo
- [x] Signed up for gitpod through github
- [x] Signed up for github codespaces through github
- [x] Created Domain name: [cruddit.link](cruddit.link)
- [x] Created AWS account
- [x] Created free tier lucid chart account under both emails

TO-DO Post Stream/Homework Assignments
---------------
- [x] Create an admin IAM user
  - still working to understand difference between root and iam (challenge says to destroy root, but how would you do billing stuff after)
- [x] Create Budget and Billing Alarm
  - Created a "no-spend" budget and a $20 budget, also created an alarm for when $10 is passed
- [x] Install AWS CLI into GitPod environment
  - installed AWS CLI into gitpod, persisted change by editng gitpod yaml
- [x] Generate AWS creds and persist in gitpod
  - Generate AWS credentials for admin user and stored in envars gitpod
- [x] Opened and tested AWS cloud shell as an alternative
  - Ran/explored various AWS commands in cloudshell 
- [x] Watched associated topic videos on security and billing and took knowledge assessment quizes
  - Security
  - Billing
- [x] Developed lucid chart diagrams for conceptual and logical diagrams
  - Cruddur Conceptual Diagram
  - Cruddur Logical Diagram


Week 0 HW Product Links
---------------
- [Cruddur Conceptual Diagram Shareable LucidChart Link](https://link-url-here.org](https://lucid.app/lucidchart/2e4e7b8a-9fb6-46eb-b995-ea45c0e2e1d6/edit?viewport_loc=-1010%2C-93%2C3657%2C1467%2C0_0&invitationId=inv_fa7c4e6d-3c5c-48ba-855a-55ad8f99aaf8))
- [Cruddur Logical Diagram Shareable LucidChart Link](https://link-url-here.org](https://lucid.app/lucidchart/25aaa6a6-c374-4d0f-a1d7-d62768cb2545/edit?viewport_loc=-106%2C32%2C2402%2C964%2C0_0&invitationId=inv_fdca318f-d1ed-40e3-a0c1-9b472ca43637))
- NOTE: PDFs posted in jornal folder in github as well

NOTES
---------------
Set environment variables (envars) in linux
export NAME=VALUE
Set environment variables in gitpod to persist securely
gp env foo=bar
