# Security Policy

## Supported Versions

This GitHub Actions template is intended to be used as a reference for other Go repositories. We recommend always using the latest version of the template. Currently, we support:

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

We take the security of our GitHub Actions templates seriously. If you discover any security issues, please follow these steps:

1. **Do not** disclose the vulnerability publicly.
2. Send a detailed report to our security team at [security@franchb.com](mailto:security@franchb.com).
3. Include the following in your report:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Any suggested fixes (if applicable)

Our security team will acknowledge your email within 48 hours and provide a more detailed response within 5 business days. This response will include the next steps in handling your report.

## Security Considerations

When using this GitHub Actions template in your Go repositories, please keep the following security considerations in mind:

1. **Secrets Management**: Ensure that you're properly managing secrets and sensitive information. Never hardcode secrets in your workflow files.

2. **Least Privilege Principle**: Configure your GitHub Actions with the minimum required permissions to perform their tasks.

3. **Dependency Management**: Regularly update and audit your dependencies, including those used in the GitHub Actions workflows.

4. **Code Review**: Always review changes to the workflow files as meticulously as you would review application code.

5. **Use Trusted Actions**: When incorporating additional actions, use only trusted and well-maintained actions from the marketplace.

## Security Updates

We strive to keep our GitHub Actions templates secure and up-to-date. When security updates are necessary, we will:

1. Release a new version of the template with the security fixes.
2. Update the README.md with information about the security update.
3. If the vulnerability is severe, we may directly notify repositories known to be using our template.

## Contributions

We welcome contributions to improve the security of our GitHub Actions template. If you have suggestions or improvements, please open an issue or submit a pull request.

Thank you for helping keep our GitHub Actions template and the repositories using it secure!
