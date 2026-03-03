output "cloud_run_service_url" {
  value       = google_cloud_run_v2_service.default.uri
  description = "The URL of the deployed Cloud Run service"
}

output "artifact_registry_repository_name" {
  value       = google_artifact_registry_repository.repo.name
  description = "The name of the Artifact Registry repository"
}
