from aws_cdk import (
    core,
    aws_ec2 as ec2
)

class VpcStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a VPC
        self.vpc = ec2.Vpc(
            self, "DjangoAppVpc",
            max_azs=2,  # Spread across 2 Availability Zones
            nat_gateways=1
        )
