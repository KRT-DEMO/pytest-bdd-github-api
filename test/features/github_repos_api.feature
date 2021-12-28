@githubAPITest
Feature: GitHub API

	As a github user,
	I want to be able to call the Github API to Create new Repositories,
  	Get User Details, and Delete Repositories,
	So that the user doesn't have to use the github web UI

@smoke @get
Scenario: GET Call returns 200
	Given the user executes a GET User call
	Then the response status code is "200"