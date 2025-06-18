# Personal Portfolio Website

This is the source code for my personal portfolio website! The website showcases my background, interests, and contact information, along with a visitor counter that utilizes AWS.

## Features

- **Responsive Design:** Built with semantic HTML and CSS for clean and professional visuals.
- **Navigation:** Smooth anchor links to Home, About, and Contact sections.
- **About Section:** Details on my education, interests, and hobbies.
- **Contact Section:** Email, phone number, and social media links (Instagram, LinkedIn, GitHub).

## AWS Integration

I have included a total visitor counter using AWS Services.

Services used:
  - **API Gateway**
      This exposed an API Endpoint to the Lambda Function
  - **AWS Lambda**
       This function tracks the total visitor count and stores it in a DynamoDB Table.
  - **Dynamo DB**
        This stores the visitor count in a DynamoDB table.

This entire integration demonstrates the use of simple services for a serverless architecture to be embedded on the site.

## Lambda Function

The Lambda function (`visitorCounter.py`) performs the following:

- On GET: fetches current count from DynamoDB.
- On UPDATE: increments and saves the count back.

## API Gateway

Configured to route HTTP GET requests to the Lambda function securely.

## DynamoDB

A single table with:
- Primary key: `siteId`
- Attribute: `visitorCount` (Number)

---

### Usage

The frontend calls this API with a delay to avoid false increments on every refresh.

## Deployment

Option 1. Link in Github Repository

## Credits

  Font Awesome for Social Media and AWS Icons
