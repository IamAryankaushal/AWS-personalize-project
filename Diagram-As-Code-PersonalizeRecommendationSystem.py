from diagrams import Diagram,Cluster,Edge
from diagrams.aws.analytics import Kinesis, KinesisDataFirehose, EMR, Glue, Athena
from diagrams.aws.compute import Lambda,EC2
from diagrams.aws.database import Dynamodb,RDS
from diagrams.aws.integration import SQS,Eventbridge
from diagrams.aws.ml import Personalize
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.storage import S3
from diagrams.aws.general import Users
from diagrams.aws.mobile import APIGatewayEndpoint
from diagrams.aws.management import Cloudwatch
from diagrams.aws.security import Cognito

# Set Diagram Attributes
graph_attr= {
    "fontsize": "30",
    "bgcolor": "white",
    "margin": "0",
    "pad": "0.5"
}

with Diagram("AWS IT Service Recommendation System Architecture",
            show=False,
            filename="aws_recommendation_system",
            direction="TB",
            graph_attr=graph_attr):

    # Define User Layer
    users = Users("Enterprise IT Users")
    
    # Define Frontend Layer
    with Cluster("Front-End Layer"):
        api = APIGateway("API Gateway")
        cdn = CloudFront("Content Delivery")
        auth = Cognito("Authentication")

    # Define Application Layer
    with Cluster("Application Layer"):
        rec_api = APIGatewayEndpoint("Recommendation API")

        with Cluster("Recommendation Services"):
            rec_lambda = Lambda("Recommendation Engine")
            personalization = Personalize("Personalization")
                
        with Cluster("User Profile Service"):
            profile_lambda = Lambda("Profile Manager")
            user_db = Dynamodb("User Profiles")
    
    # Define Data Processing Layer
    with Cluster("Data Processing Layer"):
        with Cluster("Real-time processing"):
            events = Eventbridge("Event Bus")
            streams = Kinesis("Data Streams")
            firehose = KinesisDataFirehose("Firehose")

        with Cluster("Batch Processing"):
            glue = Glue("ETL Jobs")
            emr = EMR("Spark Processing")
    
    # Define Storage Layer
    with Cluster("Storage Layer"):
        raw_bucket = S3("Raw Data")
        processed_bucket = S3("Processed Data")
        service_db = RDS("Service Catalog")
        data_lake = S3("Data Lake")
    
    # Define Analytics Layer
    with Cluster("Analytics & Monitoring"):
        dashboard = Cloudwatch("Dashboards")
        analytics = Athena("Query Engine")

    # Define connections
    users >> cdn >> api
    users >> auth >> api

    api >> rec_api >> rec_lambda

    rec_lambda >> personalization
    rec_lambda >> user_db

    profile_lambda >> user_db
    api >> profile_lambda

    # Real-time data flow
    api >> events >> streams >> firehose >> raw_bucket

    # Batch processing flow
    raw_bucket >> glue >> processed_bucket
    raw_bucket >> emr >> processed_bucket

    # Data access patterns 
    processed_bucket >> data_lake
    data_lake >> analytics >> dashboard

    # Model training flow
    processed_bucket >> personalization

    # Service catalog access
    rec_lambda >> service_db

    # Feedback loop
    api >> Edge(color="red", style="dashed") >> events