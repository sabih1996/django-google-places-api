from aws_cdk import (
    core,
    aws_ecs as ecs,
    aws_ec2 as ec2
)

class EcsClusterStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, vpc: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # ECS Cluster
        self.cluster = ecs.Cluster(self, "DjangoAppCluster", vpc=vpc)
