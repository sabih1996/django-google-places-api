from aws_cdk import (
    core,
    aws_rds as rds,
    aws_ec2 as ec2
)

class DatabaseStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # RDS Instance
        self.database = rds.DatabaseInstance(
            self, "DjangoAppDatabase",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_13_3
            ),
            vpc=vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            )
        )
