Title: Creating Effective Tickets to get work done
Date: 05/24/2024
Authors: ptyagi
Category: Leadership
Tags: Leadership, New Manager
Summary: Creating Effective Tickets to get work done

# Creating Effective Tickets

These days most of the organizations either small or large rely on Jira, Trello, Asasna or similar tools to plan a features and track their progress to deliver the value to the customers. The various tools refers a 'ticket' with different names. For example, in Jira a ticket is known as 'Issue' whereas a ticket is referred as 'Card' in Trello tool. 
To keep things simple, I'll use the word 'ticket' to keep this article focused on planning a feature without getting lost in the tooling specific vocabulary. I would use the term 'Creating Ticket' as a tool to break-down a feature into smaller actionable work-items that eventually lead to feature completion and hence delivering value to customers or end-users.

In this article, I'll share my understanding of creating effective ticket, discuss the common ticket types and their main attributes that make a ticket effective.
 

## What is an Effective Ticket?

To put simply, an effective ticket is the one that clearly communicates the necessary information to ensure that the underlying work can be understood and completed efficiently by the assignee.

## Types of Ticket
In my experience when planning a feature, there are three types of tickets that can be used to keep things simple while creating just right amount of abstraction when breaking down bigger work items into single actionable units. I frequently use following three types of tickets (or Issue types in Jira tool): 
1. Epic (or User Story)
2. Task
3. Bug

An **Epic** ticket is the one that contains the one slice of functionality towards the big picture feature. Depending on how big a feature is, it can be sliced into multiple Epics. Consider an Epic as the 'brick wall' or 'window' of a lego house. I tend to use Epic and User Story interchangeably based on the size of a feature. Epic is a collection of multiple User Stories. I've used User Story and Sub-Task structure in several projects. However, I found it effective to use Epic to describe a slice of feature and underlying Tasks contributing towards it.

A **Task** ticket is the smallest actionable unit of work that contributes towards the completion of Epic. 

A **Bug** is self-explanatory. They could the gaps in the expected functionality. There may not be any bugs when starting to build a new feature. However, as soon as a new feature either goes through the testing phase or in end-user hands, its quite normal to discover few expected or un-expected behaviors that needs to be worked on.

Let's take a sample feature of building profile page for account management in a Jira-like web application, to guide the discussion of this article. 

This feature "Profile page for account management" can be split into multiple Epics. First, a profile page user-interface design is needed. Second, a functional user-interface that user can interact with. Third, a backend component and API (Application Programming Interface) integration to store the user information for later retrieval. Fourth, quality assurance and testing. Fifth, user documentation and internal documention, etc..etc. There's a good chance that different technical expertise may be needed to execute each of the Epic. For example, designing the Profile page would require UX designing skills, front-end skills like React for implementing the page and backend skills for developing APIs.

Okay, let's go back to identifying top three Epics. For example, these first three Epic could focus on designing progile page and implementing page and developing APIs to make this page functional.

Example Epics could look like below:

1. Epic #1: Design profile page UI
2. Epic #2: Develop backend API for profile management
3. Epic #3: Develop front for profile page


## Attributes of an Effective Ticket 

An effective ticket is critical for clear communication and successful task completion. Based on my observations, the following four attributes contribute to a well-written ticket that is easily consumable by an assignee and has a high success rate of on-time completion. The following attributes can be used across the Epic, Task and Bug types.

* Summary or Title
* Description
* Acceptance criteria
* Verification & Testing (Optional)

### Summary (or title)

A concise and descriptive title that summarizes the issue or task. The title should quickly convey the essence of the task to anyone reading it.

Example: "Implement user profile page for account management."

### Description

The description should provide detailed information about the ticket, addressing the What, Why, and How of the task. This ensures the assignee understands the scope, importance, and approach to the task. Let's review each of these one by one.

#### The 'What'
Clearly state what the ticket is about. This helps to set the boundaries and expectations of the task.

Example: "The task is to develop a user profile page where users can view and edit their personal information."

#### The 'Why'
Explain why this task is important or needed. This provides context and motivation, helping the assignee understand the significance of their work.

Example: "The user profile page will enhance the user experience by allowing users to manage their personal information directly. This feature is critical for user satisfaction and retention."

#### The 'How'
Outline how the task might be done or suggest solutions. Providing a high-level plan or approach can guide the assignee and ensure alignment with the project’s goals.

Example:

* Design the user interface for the profile page.
* Develop the backend API to fetch and update user information.
* Integrate the frontend with the backend API.
* Implement validation for input fields.
* Ensure the page is responsive and works on different devices.

### Acceptance Criteria
Define what successful completion looks like. Clear acceptance criteria set the standards for when a task can be considered done and help prevent misunderstandings.

Example:

* Users can view their personal information (name, email, profile picture, etc.).
* Users can edit their personal information and save changes.
* Input validation is enforced (e.g., valid email format, mandatory fields).
* The page design adheres to the company's UI/UX standards.
* The page is responsive and functional across different devices (desktop, tablet, mobile).
* All changes are logged and can be audited for security purposes.

### Verification & Testing
This section includes verifying what was agreed upon. Although optional, it is highly recommended to outline how the task will be tested to ensure all acceptance criteria are met.

Example:
* Conduct usability testing to ensure the profile page is user-friendly.
* Perform unit and integration tests to validate that the API functions correctly.
* Check input validation rules by entering various data formats.
* Test the responsiveness of the page on different devices and screen sizes.
* Review the audit logs to ensure all changes are correctly recorded.


## Examples of Poorly vs Effectively written Jira Tickets

Before I close, it will be worthwhile to see few examples of each type of ticket discussed so far, comparing poorly written vs well-written

### [Example 1] Epic: Develop Profile Page for Account Management
Below is the example of a poorly written vs Effectively written Epic ticket. Usually, poorly written tickets don't have enough information to make the ticket actionable. They don't have clear acceptance criteria or don't have them at all.

***Poorly Written Epic Ticket***
The title and description of this Epic doesn't contain much information about what is being created and why is it needed. The acceptance criteria is very loose since it doesn't provide what's expected from this page. The verification criteria doesn't give details for assignee to verify the completeness and correctness either.

**Title:** Profile Page

**Description:** Make a profile page.

**Acceptance Criteria:** 

* Page is created.
* Users can use it.

**Verification and Testing:** 

* Check the page.


***Effectively written Epic Ticket***
In this example of Epic, the description contains the background context of what is being asked for and its justification from end-user perspective. The 'How' part is the overall scope of the feature that needs to be taken into consideration when doing granual level planning and splitting work further into Task type tickets.

**Title:** Develop Profile Page for Account Management

**Description:**

***What:*** Create a comprehensive profile page that allows users to view and edit their personal information, change their passwords, and manage other account settings.

***Why:*** Enhance user experience by providing a centralized place for managing account details.

***How:*** Design the UI, develop the backend API, implement the frontend, conduct QA testing, and create documentation.

**Acceptance Criteria:**

* Users can view and edit their personal information.
* Users can change their passwords.
* Users can manage account settings.
* All features are fully tested and documented.

**Verification and Testing:**

* Verify that the profile page meets design specifications.
* Test all functionalities to ensure they work as expected.
* Review documentation for completeness and accuracy.


### [Example 2] Task: Develop Frontend for Profile Page

Below is the example of a Task type of ticket. This Task could further be split into many other Tasks. However, to spare the implementation level details this ticket assumes that developing the Profile page UI in one ticket. The acceptance criteria helps to guide the adherence of the end to end functionality whereas verification and testing ensures the correctness and accuracy achieved.

***Poorly Written Task Ticket:***

**Title:** Frontend Profile Page

**Description:** Make the frontend for the profile page.

**Acceptance Criteria:** N/A

**Verification and Testing:** N/A

***Effectively written Task Ticket***

**Title:** Implement Frontend for Profile Page

**Description:**

***What:*** Implement the frontend components for the profile page based on the approved design. ***Note*** Add link to approved design or attach screenshot alongwith details on each UI component.

***Why:*** To allow users to interact with the profile page and manage their account information.

***How:*** Use React to build the components, ensure responsiveness, and integrate with the backend API.

**Acceptance Criteria:**

* Frontend components are implemented according to the design.
* The profile page is responsive and works on various devices.
* The frontend successfully communicates with the backend API.

**Verification and Testing:**

* Verify the layout and styling match the design.
* Test the profile page on different devices and screen sizes.
* Confirm data is correctly fetched from and sent to the backend API.
* ***Note*** Add references to front-end testing standards followed in your team


### [Example 3] Bug: Error Saving Profile Information
Let's checkout an example of poorly written vs effective bug ticket.   

**Poorly written Bug Ticket**

This ticket doesn't have descriptive title. It's hard to know from title and description about the issue let alone to fix it. Assignee likely will spend extra time to understand what's being asked to fix and where is the error occurring. They will rely on enormous Slack messages exhanges or 1-on-1 conversations just to gather the information on what error is being observed. Even after they fix it, they will likely to remain confused about whether they fixed the originally reported issue. 

**Title:** Error
**Description:** There is an error.
**Acceptance Criteria:** N/A
**Verification and Testing:** N/A


***Effectively written Bug Ticket***

Title for the ticket is self-explainatory. Assignee immediately knowns which part of the codebase they would like to start on. The description clearly mentions details on error and the severity of issue and its impact on customers. The 'how' piece explicitly sets the expectations for assingee on the action plan. Once issue has been resolved there is a check-list in the form of acceptance criteria before moving this ticket into done column. There are verification and testing steps provided to ensure that the fix has been tested reliably.  

**Title:** Error Saving Profile Information

**Description:**

***What:*** When attempting to save changes to the profile information, users receive a "500 Internal Server Error" message.

***Why:*** This prevents users from updating their profile information, which impacts user experience and functionality.

***How:*** Investigate the error, identify the root cause, and implement a fix to ensure changes can be saved successfully.

**Acceptance Criteria:**

* The "500 Internal Server Error" is resolved.
* Users can successfully save changes to their profile information without errors.
* The fix is tested and verified.

**Verification and Testing:**

* Reproduce the error by following the steps provided. ***Note***: Add steps to recreate error
* Implement the fix and verify the error is resolved. ***Note***: The fix can be verified against a pre-existing testplan, if any.
* Test saving profile information under various conditions to ensure reliability. ***Note***: Various conditions can involve development, sandbox and production environment or load/scale testing.


# References

1. [Jira Issue Types](https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-types/)
2. [Trello Card](https://trello.com/guide/trello-101)


---


***Liked the article? Let me know with 👏👏👏***

Couldn't find a topic of interest? Please leave comments or [email me](mailto:ptyagicodecamp@gmail.com) about topics you would like me to write!

Follow me at [Medium](https://medium.com/@ptyagicodecamp)
Follow me at [LinkedIn](https://www.linkedin.com/in/priyankatyagi)
