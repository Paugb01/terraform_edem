provider "google" {
    project = var.project_id
    region = var.region
    zone = var.zone
}

terraform {
    backend "gcs" {
        bucket = "terraform-bucket-edem"
        prefix = "terraform/state"
    }
}