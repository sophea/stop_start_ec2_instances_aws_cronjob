# stop_start_ec2_instances_aws_cronjob
stop_start_ec2_instances_aws_cronjob using python3 script. 

- Assume that you have some ec2 instances

What you will do in AWS Console as the following :
- create lamdba function with python3 language
- create Role with policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Start*",
        "ec2:Stop*"
      ],
      "Resource": "*"
    }
  ]
}

```

- create CloudWatch Event

See more details in this references : https://docs.google.com/document/d/16wA_TiIT7foQRbA7hGLsWYLnVuErZ7i3ECyeWD1ZwmE/edit?usp=sharing


