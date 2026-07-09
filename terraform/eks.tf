module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"

  cluster_name    = "fastapi-eks"
  cluster_version = "1.31"

  cluster_endpoint_public_access = true

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  enable_cluster_creator_admin_permissions = true

  eks_managed_node_groups = {

    general = {

      desired_size = 2
      min_size     = 2
      max_size     = 3

      instance_types = ["t3.medium"]

      capacity_type = "ON_DEMAND"
    }
  }

  tags = {
    Environment = "Production"
    Terraform   = "true"
    Project     = "production-devops-fastapi"
  }
}