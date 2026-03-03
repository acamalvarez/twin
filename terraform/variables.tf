variable "project_id" {
  type        = string
  description = "The GCP Project ID where the resources will be created."
}

variable "region" {
  type        = string
  description = "The GCP region to deploy resources to."
  default     = "us-central1"
}

variable "google_api_key" {
  type        = string
  description = "The Google API key to be passed as an environment variable to the Cloud Run service."
  sensitive   = true
}
