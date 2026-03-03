terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Enable required APIs
resource "google_project_service" "run_api" {
  project = var.project_id
  service = "run.googleapis.com"

  disable_on_destroy = false
}

resource "google_project_service" "artifact_registry_api" {
  project = var.project_id
  service = "artifactregistry.googleapis.com"

  disable_on_destroy = false
}

# Create an Artifact Registry repository for Docker images
resource "google_artifact_registry_repository" "repo" {
  location      = var.region
  repository_id = "twin-repo"
  description   = "Docker repository for Twin application"
  format        = "DOCKER"
  project       = var.project_id

  depends_on = [google_project_service.artifact_registry_api]
}

# Create the Cloud Run service
resource "google_cloud_run_v2_service" "default" {
  name     = "twin-service"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      # Placeholder image, to be updated by CI/CD pipeline after building and pushing to Artifact Registry
      image = "us-docker.pkg.dev/cloudrun/container/hello"

      env {
        name  = "GOOGLE_API_KEY"
        value = var.google_api_key
      }

      ports {
        container_port = 8080
      }
    }
  }

  depends_on = [google_project_service.run_api]
}

# Allow unauthenticated access to the Cloud Run service
resource "google_cloud_run_v2_service_iam_member" "public_access" {
  location = google_cloud_run_v2_service.default.location
  project  = google_cloud_run_v2_service.default.project
  name     = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
