var app = angular.module('deckGen', []);

app.controller('deckSelect', function($scope,$location) 
{
	$scope.shit="none";
	$scope.newDeck= function (color)
	{
		$location.url('/'+ color +'Deck');
	};
});