---
tags: [AWS Services]
title: Practice Test 1
created: '2020-08-17T18:35:46.987Z'
modified: '2020-08-18T01:47:08.477Z'
---

# Practice Test 1

- Took a practice test to check my baseline understanding of the topics on this exam.
- Failed with a result of **55% correct**.
- Spent 2 hours and 10 minutes in total (took breaks, :cat: wanted food)

## Domain 1: Resiliency

- 25 questions
- 52% Correct (Failing)

TODO: Review results, add notes on topics

## Domain 2: Security

- 19 questions
- 53% Correct (Failing)

TODO: Review results, add notes on topics

## Domain 3: High-Performance

- 15 questions
- 60% Correct (Failing)

### Question 8 :x:

- You are using a combination of API Gateway and Lambda for the web services of your online web portal
- It is expected that your web portal will receive a massive number of visitors all around the globe
- How do you protect your backend system?

**TODO**

Use throttling limits in API Gateway

**Notes**

- AWS API Gateway provides controls for throttling
- Throttling limits can be set for standard rates and bursts.
- Throttling ensures that calls to the Amazon EC2 API do not exceed the maximum allowed API request limits.

### Question 11 :x:

- A global IT company with offices around the world has multiple AWS accounts
- set up a solution that centrally manages their AWS resources
- allow them to procure AWS resources centrally and share resources such as AWS Transit Gateways, AWS License Manager configurations, or Amazon Route 53 Resolver rules across their various accounts

**TODO**

- Consolidate accounts using AWS Organizations
- Use AWS Resource Access Manager (RAM) service to share resources between AWS accounts

**Notes**

- AWS Control Tower is the easiest way to set up and govern a new, secure, multi-account AWS environment
- AWS ParallelCluster is an AWS-supported open-source cluster management tool that makes has controls for deploying and managing High-Performance Computing (HPC) clusters on AWS.
- AWS IAM allows you to delegate access to resources that are in different AWS accounts, but it's a tedious process most of the time.
- AWS Organizations allows you to manage multiple AWS Accounts
- AWS Resource Access Manager (RAM) service to easily and securely share your resources with your AWS accounts

### Question 14 :heavy_check_mark:

- App uses DynamoDB table
- Implement a "follow" feature, where users can subscribe to certain updates made by other users
- Users receive email notifications

**TODO**

- Enable DDB Stream
- create an AWS Lambda function
- Set up permissions for the Lambda Function
- lambda will process data from DDB Stream and will write to an SNS Topic that will notify subscribers

**Notes**

- A DynamoDB Stream is an ordered flow of information about changes to items in an Amazon DynamoDB table. When you enable a stream on a table, DynamoDB captures information about every modification to data items in the table.
- DynamoDB Streams are not enabled by default. Make sure you turn them on if you need to.
- The DynamoDB Accelerator (DAX) feature is primarily used to significantly improve the in-memory read performance of your database

### Question 16 :heavy_check_mark:

store most frequently used data in an in-memory data store to improve retriaval response time of a web app

**TODO**

use ElastiCache

**Notes**

- Amazon ElastiCache has controls for deploying, operating, and scaling an in-memory data store
- DynamoDB is a managed, NoSQL, document/key-value database
- AWS RDS is a relational database
- AWS Redshift is a data warehouse service

### Question 19 :heavy_check_mark:

- app hosted on EC2
- app consumes messages from SQS queue
- app posts to SNS topic when process is complete (finished processing messages in SQS)
- app sending too many messages

**Root** Cause

App likely not deleting messages in SQS queue once it has finished processing the messages.

**Notes**

- Always remember to delete SQS messages once you're done processing them
- 3 components to messaging architecture
  - the components in the distributed system (producers/consumers)
  - the messaging queue
  - the messages in the queue

### Question 24 :heavy_check_mark:

- CRM application in an autoscaling EC2 group, on-demand pricing
- app is used primarily 9am-5pm
- users noticing slowdown in the morning, no slowdown later in the day

**TODO**

Configure a "scheduled scaling" policy to bump the number of EC2 instances before people start showing up at 9am

### Question 26 :heavy_check_mark:

- data analytics application in AWS
- deployed to autoscaling group in EC2, on-demand pricing
- app uses mongodb
- app requires **high throughput workloads with random IO operations**
- best EBS type for MongoDB database?

**Answer**

Provisioned IOPS SSD EBS (`io1`)

**Notes**

- `gp2` is General Purpose SSD
- `io1` is "Provisioned IOPS SSD". Consistent performance in random and sequential IO operations
- `st1` is Throughput Optimized HDD
- `sc1` is Cold HDD
- The HDD EBS options deliver optimal performance only when I/O operations are **large and sequential**. Best for large streaming workloads. Low price compared to SSDs. Good for big data, data warehouses, log processing. Best when data is infrequently accessed.
- The SSD EBS options are best for small/random I/O operations. Best for transaction workloads. Critical for business applications that require sustained IOPS performace. Good for DB service workloads.

![](../attachments/AWS_EBS_Types_Chart.png)

### Question 29 :heavy_check_mark:

- new e-commerce Angular web app
- deployed to fleet of EC2 instances behind an Application Load Balancer ALB
- configured ALB to perform health checks on the EC2 instances
- what happens if an EC2 instance failed a health check?

**Answer**

The ALB will stop routing traffic to the EC2 instance

**Notes**

- ALBs will stop sending traffic to EC2 instances if they fail a health check.

### Question 36 :x:

- app uses CloudFront web distribution to serve static content to global users
- users are experiencing long wait times for logins
- some users are getting HTTP 504 errors
- reduce user login time and optimize system

**TODO**

- set up an origin failover by creating an origin group with 2 origins
- specify one origin as primary and the other as secondary
- CloudFront will automatically switch to the secondary origin when the primary origin returns specific HTTP status codes
- customize the content that the CloudFront web distribution delivers to your users using Lambda@Edge. This will allow lambda functions to execute authentication closer to each user

**Notes**

> In the given scenario, you can use Lambda@Edge to allow your Lambda functions to customize the content that CloudFront delivers and to execute the authentication process in AWS locations closer to the users. In addition, you can set up an origin failover by creating an origin group with two origins with one as the primary origin and the other as the **second origin which CloudFront automatically switches to when the primary origin fails. This will alleviate the occasional HTTP 504 errors** that users are experiencing.

- Lambda@Edge lets you run lambda functions to customize the content that CloudFront delivers, executing the functions in AWS locations closer to the user.
- You can use lambda functions to change requests and responses brokered by CloudFront between the end user and the origin

![](../attachments/CloudFront_Request_Response_Diagram.png)

### Question 42 :heavy_check_mark:

Which CloudWatch metrics are available by default for EC2 instances? Which are not?

**Notes**

- The following CloudWatch EC2 Metrics are available by default
  - CPU Utilization of an EC2 instance
  - Disk Reads activity of an EC2 instance
  - Network packets out of an EC2 instance
- The following CloudWatch EC2 Metrics are not available by default, but can be configured by installing a CloudWatch Agent on the EC2 instances.
  - Memory utilization
  - Disk swap utilization
  - Disk space utilization
  - Page file utilization
  - Log collection
- It's possible to write custom metrics in Perl using CloudWatch Monitoring Scripts (please don't do this)

### Question 48 :x:

- application uses a machine learning model
- app's workflow requries high-performance, parallel hot storage to process the training datasets concurrently
- application needs cost-effective cold storage to archive datasets that yield low profit
- best AWS storage services to use for this app?

**Answer**

- Use AWS FSx For Lustre for host storage
- Use AWS S3 for cold storage

**Notes**

- Temperature
  - Hot storage refers to the storage that keeps frequently accessed data ( hot data ).
  - Warm storage refers to the storage that keeps less frequently accessed data ( warm data ).
  - Cold storage refers to the storage that keeps rarely accessed data ( cold data ).
- Amazon FSx For Lustre is a high-performance file system for fast processing of workloads.
- Lustre is a popular open-source parallel file system which stores data across multiple network file servers to maximize performance and reduce bottlenecks.
- Amazon Elastic File System (EFS) is a fully-managed file storage service that makes it easy to set up and scale file storage in the Amazon Cloud.
- EFS supports concurrent access to data, but it does not have the high-performance ability that is required for machine learning workloads.
- AWS S3 is an object storage service.
- Amazon FSx for Windows File Server is a fully managed Microsoft Windows file system with full support for the SMB protocol, Windows NTFS, Microsoft Active Directory (AD) Integration. Amazon FSx For Windows File Server does not have a parallel file system, unlike Lustre.

### Question 51 :heavy_check_mark:

- app is a CMS hosted on an autoscaling EC2 group (on demand pricing)
- app uses Amazon Aurora as its database
- system stores file documents in various EC2 EBS volumes
- improve architecture and system performance 
- What is AWS's scalable, high-throughput, POSIX-compliant file systems?

**Answer**

EFS

> Amazon Elastic File System (Amazon EFS) provides simple, scalable, elastic file storage for use with AWS Cloud services and on-premises resources. When mounted on Amazon EC2 instances, an Amazon **EFS file system provides a standard file system interface and file system access semantics**, allowing you to seamlessly integrate Amazon EFS with your existing applications and tools. **Multiple Amazon EC2 instances can access an Amazon EFS file system at the same time**, allowing Amazon EFS to provide a common data source for workloads and applications running on more than one Amazon EC2 instance.

### Question 52 :heavy_check_mark:

- app uses cloudfront, lambda, dynamodb for backend services
- which AWS service reduces DynamoDB response times?

**Answer**

Amazon DynamoDB Accelerator (DAX)

**Notes**

- Amazon DynamoDB Accelerator (DAX) is a fully managed, highly available, in-memory cache that can reduce Amazon DynamoDB response times
- Amazon ElastiCache can be used as a database cache, but if you're trying to accelerate AWS DynamoDB (DDB), you can more easily use DAX.
- AWS Device Farm is an app testing service that lets you test and interact with your Android, iOS, and web apps on many devices at once, or reproduce issues on a device in real time.
- DynamoDB Auto Scaling is primarily used to automate capacity management for your tables and global secondary indexes.

### Question 60 :x:

- app uses an API build with Lambda and API Gateway
- app maintainers are expecting significant increase in traffic in the coming days
- protect the backend from traffic spikes

**TODO**

Enable throttling limits and result caching in API Gateway

**Notes**

- If you see a question related to protecting the backend from traffic spikes, think "throttling"
- AWS API Gateway provides throttling at multiple levels including global and by service call
- API Gateway: https://aws.amazon.com/api-gateway/faqs/

### Question 61 :x:

- containerized app running on AWS ECS cluster behind a load balancer
- app heavily uses DynamoDB
- improve db performace by distributing the workload evenly

**TODO**

Use partition keys with high-cardinality attributes, which have a **large number of distinct values for each item**.

**Notes**

> The partition key portion of a table's primary key determines the logical partitions in which a table's data is stored. This in turn affects the underlying physical partitions. Provisioned I/O capacity for the table is divided evenly among these physical partitions. Therefore **a partition key design that doesn't distribute I/O requests evenly can create "hot" partitions** that result in throttling and use your provisioned I/O capacity **inefficiently**.

- more distinct partition key values -> more even spread across the partitioned space -> better performance
- fewer distinct partition key values -> less even spread across the partitioned space -> slower performance
- a composite primary key will provide more partition for the table and in turn, improves the performance
- to increase performance of DynamoDB:
  - increase distinct partition keys
  - composite primary keys (partition key + sort key), increases partition keys

## Domain 4: Cost-Optimization

- 3 questions
- 100% correct :heavy_check_mark:

### Question 46 :heavy_check_mark:
- App hosted on AWS Fargate (ECS)
- App runs a batch job when object uploaded to S3
- "minimum number of ECS tasks" is set to `1` to save costs
- "minimum number of ECS tasks" should be adjusted based on state of bucket

**TODO**

Set up CloudWatch Event on S3 PUT/DELETE operations, adjusting the "tasks" number on the cluster accordingly

**Notes**

- Cloudwatch Events can target ECS clusters and can adjust the number of tasks on those clusters
- Always remember that CloudWatch Events and CloudWatch Alarms are totally different things.

### Question 49 :heavy_check_mark:

- Startup with an online portal
- funding is tight and you need to manage your AWS budget

**TODO**

Use "AWS Budgets" service

**Notes**

- AWS Budgets can be used to proactively keep your AWS costs in check. 
- Cost Explorer is a reactive way to check on how much money your AWS resources are using
- Cost Allocation Tags can be used to group costs, helping your organize your expsense reports
- Payment History shows past invoices

### Question 55 :heavy_check_mark:

Optimize costs related to transferring data from EC2 to S3

**Notes**

- Transferring data from EC2 to S3 within the same region costs $0
- "Transferring data from an EC2 instance to Amazon S3, Amazon Glacier, Amazon DynamoDB, Amazon SES, Amazon SQS, or Amazon SimpleDB in the same AWS Region has no cost at all." Apparently it's all block storage on the backend.

