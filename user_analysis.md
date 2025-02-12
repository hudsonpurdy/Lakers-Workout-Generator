# Lakers Project User Analysis

Theo Demetriades, Oliver Hall, Hudson Purdy, Gavin Saxer

This file provides more information about who might find this project useful and implements the CIDER technique to provide greater context to the various features provided.

## Potential Users

The project is designed to assist those interested in exercise, demonstrating why and how one would choose a particular exercise, and is designed to be a purely informational tool. With the command line interface the potential users was limited to people with some degree of computer literacy. With the Flask app, the potential users is expanded to those who understand what a URL is and how to type.

## Our Command Line Features

This project is currently equipped with two command-line functions:

- List Exercises by Muscle Group
- List Exercises by Equipment


## Our Flask App Feature

Our basic flask app is equipped with two features:

- Search exercises by muscle group by going to url /musclegroup/<muscle>
- Search exercises by equipment by going to url /equipment/<equipment>

### CIDER critique

Assumptions:

- Our app assumes users have access to a browser.
- Our app assumes users know how to enter/edit urls and how the root url can be reached.
- Our app assumes some understanding of what 404 and 500 errors are.


## CIDER analysis

### Critique

This project assumes users have access to a command line, can type, and can see/read English. It also assumes the users are interested in hypertrophy and weight training exercieses. Finally, it assumes users don't have significant disabilities that impair them from certain exercises.

### Imagine

Our assumption of an interest in weight-training exercises could exclude those who are primarily interested in cardiovascular or flexibility exercises, as our database doesn't provide those exercises.

### Design

Moving forward, to be more inclusive, the database could be expanded to include exercises beyond those meant for hypertrophy.

### Expand

After a discussion, the team identified the bias of the matrix of domination permeating the infrastructure of the project, with the implicit assumption of only able-bodied users.

### Repeat

Another important topic discussed was the assumption of able-bodiedness of our users. This could exclude a large proportion of the potential user base. The team decided that, to combat this potential failing, the project could include a filter for certain body movements the user is unable to do under resistance.

## CIDER analysis: Team Deliverable: Database

### Critique

Our database collection method has a few critical assumptions embedded in its functionality. One is that we are assuming that all equipment for exercise can be effectively represented by only a few categories, like dumbells or barbells, and the exercises that don't fall into this categorization are labeled "Other". Additionally, we assume that the user has the ability to connect to "bodybuilding.com", which might not be available in other countries, and our app would lose functionality if this website is down. A third assumption embedded in our collection methods is similar to that of equipment- our categorization of muscle groups includes assumptions about what muscle groups are relevant or what exercises effectively target those muscle groups.

### Imagine

The assumption about equipment could exclude those who have non-standard equipment and could confuse them. Additionally, the assumption that bodybuilding.com is running could exclude those that are excluded by bodybuilding.com- either everyone if it is down or people who don't have access to the website for some reason. The assumption about muscle groups could exclude those who want to target groups outside of the categories we have, or want to target those muscle groups for flexibilty or different functional reasons. 

### Design

Moving forward, we could edit our description and image functonalities to not link to bodybuilding.com, removing our app's reliance on this third-party website. We could expand our exercise and muscle group categories to include more edge-case functionalities, and give more context on the website so that users understand our assumptions and categorizations. 

### Expand

We talked about accessibility and inclusivity biases like the exclusion of users with non-standard equipment or those who can't access bodybuilding.com. Also, our categorization of muscle groups might not accommodate users with different training goals. 

### Repeat

We are excluding those with different training goals. Thus, we could either talk about what kinds of goals for users would make it helpful for them to use this project. We could also add new functionalities to look at exercises not for just hypertrophy.

## CIDER analysis: Team Deliverable: Front-End

### Critique 

We assume that any users have normal color vision and can distinctly tell the difference between purple and gold. Additionally, we assume that all users have functional eyesight and a working mouse with the ability to click in order to navigate between pages. As of the time of writing this, the results are just a list of exercises with no descriptions which assumes that users know what each exercise name means.

### Imagine

These assumptions could explude those with vision impairment disabilities. It also excludes those with limited experience with working out, as exercise names will be unknown and hold no useful information.

### Design

Moving forward, we will include links to bodybuilding.com for each exercise which will contain images and videos as well as a written description of the exercise. 

### Expand

We talked about how to address the exlusion of users with vision impairment as well as ways to make the links easy to see and access to allow users to get the most information about their exercises.

### Repear

We could add a settings button to allow switching to colorblind color schemes, but the amount of users using the website with such significant vision impairment is extremely small and as such is not a priority in the website design at this stage.
