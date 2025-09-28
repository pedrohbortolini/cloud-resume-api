output "api_endpoint" {
  description = "Invoke URL of the API Gateway"
  value       = aws_apigatewayv2_stage.default.invoke_url
}
