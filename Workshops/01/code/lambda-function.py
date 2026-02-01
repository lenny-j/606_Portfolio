# Lambda Function - TechStart Serverless Response
# This function runs on-demand when triggered (API Gateway, test event, etc.)

def lambda_handler(event, context):
    """
    AWS Lambda handler function.

    Parameters:
        event (dict): Input data passed to the function (API request, trigger data, etc.)
        context (object): Runtime information provided by Lambda

    Returns:
        dict: HTTP response with status code, headers, and body
    """
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '<h1>TechStart Inc. - Serverless Response</h1><p>Powered by AWS Lambda</p>'
    }
