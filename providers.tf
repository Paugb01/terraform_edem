provider "google" {
    project = var.project_id
    region = var.region
    zone = var.zone
}

terraform {
    backend "gcs" {
        bucket = "hackathon_nttdata"
        prefix = "terraform/state"
    }
}