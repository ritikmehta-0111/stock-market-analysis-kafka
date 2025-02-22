Ref 
------------------------------------------------------------
Youtube Video	https://www.youtube.com/watch?v=KerNf0NANMo
------------------------------------------------------------


1. How can I create EC2 instance?
    - AWS account	- mehtaritik1997@gmail.com
        
    - To launch an instance	
        - Name
        kafka-stock-market
            
        - Application & OS
        Amazon Linux 2 AMI(HVM) - kernel 5.10, SSD VolumeType (Free Tier)
            
        - Instance Type
        t2.micro (Free Tier)
            
        - Key Pair (login)
        "If you have key pair name you can select or else create new one

        - download that *.pem key to your computer and save it to your project location"
            
        Click on launch instance	

2. How to connect to this instance from windows machine ?
    click on Instance id 
    click on connect
    click on SSH client
    You will find below command :  
    ssh -i "kafka-stock-market-project-key.pem" ec2-user@ec2-3-87-73-168.compute-1.amazonaws.com
    
    "open CMD - Go to project location where you have that *.pem file & paste this ssh command
    Error:
        If you face any issue with permissions
        Keep only you as permission with full permission and remove other users"

3. How to download kafka on EC2?
    Since we are already connected to EC2 via CMD. You can run below command.
    wget https://downloads.apache.org/kafka/3.9.0/kafka_2.12-3.9.0.tgz
    tar -xvf kafka_2.12-3.9.0.tgz"

4. How to start zookeeper ?
    bin/zookeeper-server-start.sh config/zookeeper.properties

5. How to start kafka broker?
    Start kafka broker
    ----------------------------------------------------------------------------------------------------------------------------
    Duplicate the session & enter in a new console --
    export KAFKA_HEAP_OPTS=""-Xmx256M -Xms128M""
    cd kafka_2.12-3.9.0
    bin/kafka-server-start.sh config/server.properties
    ----------------------------------------------------------------------------------------------------------------------------
    
    It is pointing to private server , change server.properties so that it can run in public IP 
    ---------------------------------------------------------------------------------------------------------------------------- 
    To do this , you can follow any of the 2 approaches shared belwo --
    Do a ""sudo nano config/server.properties"" - change ADVERTISED_LISTENERS to public ip of the EC2 instance"
    ----------------------------------------------------------------------------------------------------------------------------
    
5. How to create topic?
    Create topic:
    ----------------------------------------------------------------------------------------------------------------------------
    Duplicate the session & enter in a new console --
    cd kafka_2.12-3.9.0
    bin/kafka-topics.sh --create --topic demo_testing1 --bootstrap-server 3.87.73.168:9092 --replication-factor 1 --partitions 1"
    ----------------------------------------------------------------------------------------------------------------------------
    
    Start Producer:
    ----------------------------------------------------------------------------------------------------------------------------
    bin/kafka-console-producer.sh --topic demo_testing1 --bootstrap-server 3.87.73.168:9092"
    ----------------------------------------------------------------------------------------------------------------------------
    
    Start Consumer:
    ----------------------------------------------------------------------------------------------------------------------------
    Duplicate the session & enter in a new console --
    cd kafka_2.12-3.3.1
    bin/kafka-console-consumer.sh --topic demo_testing1 --bootstrap-server 3.87.73.168:9092"
    ----------------------------------------------------------------------------------------------------------------------------
    
6. How to create S3 bucket?
    In s3 console - search for s3 bucket - give unique name - create bucket

7. How to connect to S3 bucket to local ?
    "search for IAM 
    - click on users 
    - Add user 
    - give user name (Do not select AWS management Console)
    - select Attach Policies Directly
    - select AdministratorAccess
    - user will be created.
    - Click on the user
    - Security Credentials
    - create access key
    - select Local code
    - you will get access key and secret key 


    Download the AWS cli
    - msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
    - open CMD - where /R c:\ aws
    - copy paste the value to set the PATH variable
    - aws --version
    - aws configure

    In consumer.py script:
    I need to have s3fs package insalled."

8. How to create crwaler?
    - search for Glue
    - click on crawler 
    - click on Add crawler
    - add data source"

9. How to use Athena?
    - Athena is edit to run SQL query.
    - Before you execute any query
    - we need to add temp s3 bucket to save the query result"