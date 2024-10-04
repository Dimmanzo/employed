# Employed - Job Board

[View live project here!](https://employed-931f04b674fc.herokuapp.com/)

## Project Rationale
This project was developed to address the growing need for a seamless job application process for both job seekers and employers.
It aims to streamline job searching and application management in a user-friendly environment, ultimately connecting skilled individuals with opportunities.

---

![Am I Responsive](media/responsive.png)  
_Responsive design on various screen sizes_

---

## Overview
The **Employed** platform is a user-friendly **full-stack** web application that connects **job seekers** with potential **employers**.
Users can easily **browse** through various job listings, **search** for opportunities that match their skills, and **submit** applications with just a few clicks.
On the employer side, it allows for effortless **posting** of new job openings, updating listings, and managing applications—all in one place.
This solution is designed to make the process of finding or posting jobs smooth, efficient, and accessible for everyone involved.

---

## Table of Contents
- [Project Rationale](#project-rationale)
- [Features](#features)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [User Stories](#user-stories)
- [Screenshots](#screenshots)
- [Agile Methodology](#agile-methodology)
- [UX Design](#ux-design)
- [Database Schema](#database-schema)
- [Manual Testing](#manual-testing)
- [Automated Testing](#automated-testing)
- [Lighthouse Testing](#lighthouse-testing)
- [Validation and Browser Compatibility](#validation-and-browser-compatibility)
- [Version Control and Commits](#version-control-and-commits)
- [Security Considerations](#security-considerations)
- [Deployment](#deployment)
- [Setup Instructions](#setup-instructions)
- [Technologies and Tools Used](#technologies-and-tools-used)
- [Cloning and Forking](#cloning-and-forking)
- [Credits](#credits)

---

## Features

### Existing Features
- **Employer Dashboard**: Employers can log in, post new jobs, and manage existing job listings (edit, close, or delete jobs).
- **Job Seeker Dashboard**: Job seekers can view the status of their applications and track progress, while job browsing and searching can be done on the main page.
- **Job Application Management**: Employers can view job applications, accept or reject them, and manage the status of applications.
- **Search and Filter**: Job seekers can filter jobs by type, work type, and location, as well as search by keywords in the job title, description, or excerpt.
- **Role-Based Authentication**: Employers and job seekers have different dashboard views and permissions based on their roles.
- **Closed Jobs**: Jobs that are closed are no longer open for applications, ensuring employers stop receiving applications when needed.
- **User Profile**: Implemented a user profile page where job seekers and employers can update their personal information (full name, email, phone, address, bio).
- **Prefill Application Form**: Job seekers can prefill the application form with their profile details to streamline the application process.

### Features to be Added
- **Notifications**: Implement notifications for employers when job applications are received and for job seekers when application status changes.
- **Job Alerts**: Allow job seekers to set alerts for new job postings that match their search criteria.
- **Employer Analytics**: Provide employers with analytics and insights about job postings (e.g., number of applications, views, etc.).
- **Favorite Jobs**: Allow job seekers to save jobs they’re interested in and revisit them later.
- **Email Verification**: Implement email verification during registration to ensure valid email addresses.
- **Profile Page Improvements**: Add the option for users to upload a profile picture, enhancing personalization and user experience.
- **CV and Cover Letter Upload**: Users will have the option to upload their CV or cover letter directly when applying for jobs.

---

## Known Issues
- Users currently cannot edit their applications once submitted; this feature is planned for future updates.
- Job seekers do not receive immediate notifications when a job application status changes; notifications will be implemented in future releases.
- All known issues will be monitored as the project progresses to ensure timely updates and enhancements.

---

## Future Improvements
- Improve the notification system to keep users informed of job postings, application statuses, and other relevant updates.
- Enhance the employer dashboard with advanced analytics for better decision-making regarding job postings.
- Introduce a more comprehensive search algorithm to provide better job matching for seekers based on skills and experience.
- Develop a mobile application to provide easier access to job listings and applications on the go.
- Implement additional filters in job search to allow job seekers to refine their search further.
- Enhance the UI/UX based on user feedback to improve overall user satisfaction.

---

## User Stories
- As a **Job Seeker**, I can **apply for a job** so that **I can offer my services to an employer**.
- As a **Job Seeker**, I can **browse available jobs** so that **I can find work that matches my skills**.
- As an **Employer**, I can **post a job listing** so that **I can hire an employee for a specific task**.
- As a **Registered User**, I can **log in and log out of my account** so that **I can access personalized features**.
- As a **Job Seeker or Employer**, I can **create an account** so that **I can access the platform’s features**.
- As an **Employer**, I can **delete my job postings** so that **I can remove outdated or irrelevant listings**.
- As an **Employer**, I can **close job postings when the hiring process is complete** so that **I stop receiving applications for that position**.
- As an **Employer**, I can **accept or reject job applications** so that **I can manage the hiring process effectively**.
- As an **Employer or Job Seeker**, I can **view a dashboard where I can see all my job posts and applications** so that **I can manage them or check their status**.
- As a **Job Seeker**, I can **see the status of my job applications** so that **I know if I have been selected or rejected**.
- As a **Job Seeker**, I can **search for jobs by keywords** so that **I can quickly find relevant opportunities**.
- As a **Registered User**, I can **update my profile details** so that **my information stays accurate**.
- As an **Employer**, I can **edit my job listings** so that **I can make updates to the job details**.
- As a **Job Seeker**, I can **upload my CV and cover letter when applying for jobs** so that **I can present my qualifications and experience efficiently**.
- As a **User**, I can **upload a profile picture to personalize my account** so that **my profile reflects my identity and enhances my experience on the platform**.
- As a **User**, I can **verify my email during registration** so that **I can ensure my account is securely created and prevent unauthorized access**.
- As a **Job Seeker**, I can **save jobs I’m interested in** so that **I can easily revisit and apply for them later**.
- As an **Employer**, I can **view analytics on my job postings (e.g., number of applications, views, etc.)** so that **I can assess the effectiveness of my listings and make data-driven decisions**.
- As a **Job Seeker**, I can **set alerts for new job postings that match my search criteria** so that **I can be notified of relevant opportunities without constantly checking the platform**.
- As a **Job Seeker**, I can **receive notifications when the status of my job application changes** so that **I can stay updated on my application progress**.
- As an **Employer**, I can **receive notifications when job applications are submitted** so that **I can quickly review and manage incoming applications**.
- As an **Employer**, I can **rate or review job seekers after a project** so that **other employers can see their work quality**.

---

## Screenshots

### Home Page
![Home Page](media/homepage.png)
_The homepage provides users with easy navigation to browse available job listings._

### Job Seeker Dashboard
![Job Seeker Dashboard](media/jobseeker-dashboard.png)
_Job seekers can view the status of their applications and track the progress of their job search._

### Employer Dashboard
![Employer Dashboard](media/employer-dashboard.png)
_Employers can post and manage job listings as well as view applicant submissions._

### Job Details Page
![Job Details](media/job-details.png)
_Job seekers can view detailed job descriptions and apply directly._

---

## Agile Methodology

This project followed an Agile development process, utilizing **GitHub Projects** to manage the planning and tracking of user stories and tasks. The Kanban board was employed to prioritize features and track progress through various stages of development.

You can access the Kanban board [here](https://github.com/users/Dimmanzo/projects/3).

- **Kanban Board**: The entire development process was managed using a Kanban board, ensuring that each task moved through the stages of "To Do", "In Progress", and "Done". 

- **Milestones**: Key milestones were established to segment the project into manageable phases, ensuring timely completion of essential features. Each milestone focused on specific functionalities, guiding towards clear goals.

- **Labels**: Various labels were used to categorize tasks, such as "Must Have", "Should Have", "Could Have". This classification helped prioritize features based on urgency and importance, facilitating better planning and execution.

- **User Stories**: Each feature was mapped to a user story and broken down into smaller, actionable tasks. This approach allowed for clearer task assignment and tracking, ensuring that all aspects of user requirements were addressed effectively.

![Kanban Board](media/kanban.png)
_Kanban Board for Employed project_

![Kanban Board](media/milestones.png)
_Milestones for Employed project_

![Kanban Board](media/labels.png)
_Labels for Employed project_

![Kanban Board](media/user-story-tasks.png)
_User Story Tasks for Employed project_

---

## UX Design

During the design phase, wireframes were created to ensure the user interface would be intuitive, responsive, and easy to navigate.

- **Wireframes** were designed using **Balsamiq**.

![Home Page Wireframe](media/wireframe.png)
_PC - Homepage, Mobile - Register wireframes_

![Job Seeker Dashboard Wireframe](media/wireframe-js-dashboard.png)
_PC - Homepage, Mobile - Register wireframes_

![Employer Dashboard Wireframe](media/wireframe-employer-dashboard.png)
_PC - Homepage, Mobile - Register wireframes_

![Job Application Page Wireframe](media/wireframe-application.png)
_PC - Homepage, Mobile - Register wireframes_

---

## Database Schema

The data model for this project includes key entities such as users, profiles, jobs, and applications, all connected through foreign keys to create relationships between employers, job seekers, job listings, and applications.

- **Database schema** was designed using **dbdiagram.io**.

![Database Schema](media/db-schema.png)  
_Overview of all DB models_

- **Users**: This table stores core user information, including username, email, and password. 
- **Profiles**: This table extends the User model and stores additional information such as user roles (either "Employer" or "Job Seeker") and contact details (full name, phone number, address, and bio).
- **Jobs**: This table contains job postings created by employers. Each job includes details such as the title, description, location, job type (e.g., full-time, part-time), and work type (e.g., remote, on-site, hybrid). Each job is associated with an employer (via a foreign key reference to the users table).
- **Applications**: This table tracks job applications submitted by job seekers for specific jobs. It includes fields like the applicant's name, contact information, and a cover letter, as well as the application status (e.g., under review, accepted, rejected). Each application is linked to both a job and a user (the applicant).

---

## Manual Testing

Extensive manual testing was conducted to ensure proper functionality of all key features.

| Test Case | Expected Outcome | Result |
| --------- | ---------------- | ------ |
| Employer posts a job | Job appears on main job listings | ✅ |
| Job Seeker applies for job | Application successfully submitted | ✅ |
| Employer closes a job | No new applications accepted | ✅ |
| Job search | Relevant jobs displayed based on search query | ✅ |
| Filter jobs by type, work type, location | Only relevant jobs are displayed | ✅ |
| Employer edits job details | Job details are updated | ✅ |
| Role-based access | Employers cannot access job seeker-only features | ✅ |
| Admin can manage users and jobs from admin panel | Admin functionalities work correctly | ✅ |
| Job status change (Open/Closed) | Job status is updated correctly, closed jobs not accepting applications | ✅ |
| Prefill Application Form | Profile data (name, email, phone, address) is correctly prefilled | ✅ |
| User Profile Update | Users can successfully update their profile details (full name, email, phone, address, bio) | ✅ |
| Prevent login/register for authenticated users | Logged-in users are redirected from login/register pages to the dashboard | ✅ |
| Form Submission Validations | Ensure that all required fields are filled out in job applications, preventing submission with empty fields | ✅ |

---

## Automated Testing

Automated testing has been implemented using Django’s built-in testing framework, including unit tests for views, models, and forms. The tests cover essential functionality across the Dashboard, Jobs, and Profiles apps.

### Types of Unit Tests Implemented:
- **Dashboard Tests**: 
  - Verified that the employer and job seeker dashboards render correctly.
  - Tested that job seekers can view and withdraw their applications.

- **Job Tests**: 
  - Ensured job listings can be created, viewed, and applied for by job seekers.
  - Validated that the job list view displays jobs as expected.
  - Confirmed that job applications are submitted, accepted, or rejected appropriately.

- **Profile Tests**: 
  - Checked user registration, login, and logout functionalities.
  - Ensured users can update their profiles and are redirected correctly based on their roles (employer or job seeker).

### Coverage:
- Overall test coverage is approximately **85%**, ensuring that critical paths and functionalities are thoroughly tested.

### Total Tests Run:
- A total of **13 tests** were executed, covering various aspects of the application.

### Additional Planned Tests:
- **Form Validations**: Automate validation checks for required fields in job applications.
- **Additional User Interactions**: Implement tests for user feedback mechanisms, such as notifications and user role transitions.

---

## Lighthouse Testing

The performance and accessibility of the website were tested using **Google Lighthouse**.

![Lighthouse](media/lighthouse.png)  
_Performance 97, Accessibility 100, Best Practices 100, SEO 100_

---

## Validation and Browser Compatibility

All HTML, CSS, JS and Python files were tested and validated with no errors found:

- **HTML Testing**: [W3C Markup Validation Service](https://validator.w3.org/)

![HTML Validator](media/html-validator.png)  
_Tested on all pages with no errors found_

- **CSS Testing**: [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

![CSS Validator](media/css-validator.png)  
_Tested with no errors found_

- **JS Testing**: [JSHint, a JavaScript Code Quality Tool](https://jshint.com/)

![JS Validator](media/js-validator.png)  
_Tested with no errors found_

- **Python Testing**: [CI Python linter](https://pep8ci.herokuapp.com/) 

![Python Validator](media/python-validator.png)  
_Tested on all python files with no errors found_

### Browser Compatibility:
The project was tested across the following browsers to ensure compatibility:

- **Google Chrome**
- **Mozilla Firefox**
- **Microsoft Edge**

---

## Version Control and Commits

Version control was maintained using **Git** and **GitHub**. The commit history reflects small, frequent, and focused changes.

- **Commit Messages**: Each commit is meaningful and clearly describes the changes or feature implemented.
- **Commit Frequency**: Regular commits ensured that progress was consistently tracked.

---

## Security Considerations

Security features were a key focus of the development process to protect sensitive user information.

- **Environment Variables**: Sensitive information such as secret keys and database credentials are stored in environment variables.
- **Role-Based Authentication**: Access to features and content is restricted based on the user's role (employer or job seeker).
- **Password Security**: Django's built-in authentication and password hashing features are used to ensure secure login and account management.
- **Restricting Access**: Logged-in users are restricted from accessing the login and registration pages. They are automatically redirected to the dashboard when attempting to access these pages.

---

## Deployment

The project was deployed to Heroku using Git and GitHub for version control. The following steps were used to deploy the project:

1. Create a new Heroku app in the Heroku dashboard.
2. Set up **PostgreSQL from Code Institute** as the database.
3. Set up environment variables for sensitive data (SECRET_KEY, DATABASE_URL).
4. Push the project to Heroku using Git.
5. Migrate the database and create a superuser for admin access.

**Live Project**: [Deployed Site](https://employed-931f04b674fc.herokuapp.com/)

---

## Setup Instructions

To set up the project in Gitpod, follow these steps:

1. **Open Gitpod**:  
    Navigate to your GitHub repository and prefix the URL with `gitpod.io/#`. For example:  
    `https://gitpod.io/#https://github.com/yourusername/employed.git`

2. **Install dependencies**:  
    In the terminal, run:  
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**:  
    Create a PostgreSQL database and update the `DATABASE_URL` in your environment variables.

4. **Run migrations**:  
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser for admin access**:  
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:  
    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```

7. **Access the application**:  
    Open the URL provided in the terminal to view your application.

---

## Technologies and Tools Used

- **HTML**: For the structure of the website.
- **CSS**: For styling and layout.
- **JavaScript**: For interactivity and dynamic elements.
- **Django**: As the back-end framework for the project.
- **PostgreSQL**: The relational database used to store all project data.
- **Heroku**: Cloud platform used for deployment.
- **Git**: Version control system for tracking changes in the project.
- **GitHub Projects**: Project management tool for managing user stories and tasks.
- **Bootstrap**: CSS framework for responsive design and UI components.
- **Font Awesome**: Icon library used throughout the platform.
- **Balsamiq**: Wireframing tool used to create mockups for the project.
- **Gunicorn**: A WSGI HTTP Server used for running the Django application on Heroku.
- **Whitenoise**: A library for serving static files in Django, particularly in production (Heroku).
- **Django crispy forms**:  A Django package used to improve the layout and styling of forms.
- **Jinja**: Template engine that Django uses for rendering dynamic content into HTML.

---

## Cloning and Forking

### Cloning

To clone the repository:

- On GitHub.com, navigate to the main page of the repository.
- Above the list of files, click **Code**.
- Copy the URL for the repository.
- Type `git clone`, and then paste the URL you copied earlier.
- Press **Enter** to create your local clone.

### Forking

To fork the repository:

- On GitHub.com, navigate to the main page of the repository.
- In the top-right corner of the page, click **Fork**.
- Under "Owner," select the dropdown menu and click an owner for the forked repository.
- Click **Create Fork**.

---

## Credits

- **Code**: Help with Django best practices from the [Django documentation](https://docs.djangoproject.com/), Some ideas were taken from the [Code Institute](https://codeinstitute.net/)'s blog walkthrough project.
- **Bootstrap**: Used for responsive grid layout and UI components such as buttons, forms, and navigation [Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/). 
- **Media**: Icons from [Font Awesome](https://fontawesome.com/).
- **Balsamiq**: For creating wireframes to visualize the design before development [Balsamiq](https://balsamiq.com/).
- **Google Fonts**: For typography styling used throughout the website [Google Fonts](https://fonts.google.com/).
- **Heroku**: For cloud deployment and hosting [Heroku](https://www.heroku.com/).
- **dbdiagram.io**: For database structure scheme [dbdiagram.io](https://dbdiagram.io/).
- **Flaticon**: Favicon taken from [Job seeker](https://www.flaticon.com/free-icon/job-seeker_5941749?term=employment&page=1&position=1&origin=tag&related_id=5941749).