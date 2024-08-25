from aws_cdk import core
from lib.vpc_stack import VpcStack
from lib.ecr_stack import EcrStack
from lib.ecs_cluster_stack import EcsClusterStack
from lib.ecs_service_stack import EcsServiceStack

app = core.App()

# Instantiate Stacks
vpc_stack = VpcStack(app, "VpcStack")
ecr_stack = EcrStack(app, "EcrStack")
ecs_cluster_stack = EcsClusterStack(app, "EcsClusterStack", vpc=vpc_stack.vpc)
ecs_service_stack = EcsServiceStack(app, "EcsServiceStack", cluster=ecs_cluster_stack.cluster, repository=ecr_stack.repository)

app.synth()
