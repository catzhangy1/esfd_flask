'use strict';

angular.module('esfd.game', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/game', {
            templateUrl: '../static/js/game.html',
            controller: 'GameCtrl'
        });
    }])

.controller('GameCtrl',    
    ['$scope','$log', 'dataService', '$http', '$window',
    function($scope, $log, dataService, $http, $window) {
    $scope.gameReload = function() {
        $window.location.reload();
    }
    var results = new Array();
    results["correct"] = '2';
    results["location"] = 'Bermuda';
    results["image1"] = 'http://donaldmurrayexpat.com/wp-content/uploads/2014/09/Cancun-Overhead.jpg';
    results["image2"] = 'http://www.bermuda-online.org/Bermudapinkbeach2.jpg';
    results["image3"] = 'http://www.qantas.com.au/img/campaigns/2013/destination/hawaii/gallery/hawaii10-b.jpg';
    results["image4"] = 'http://www.esenciaexperiences.com/old/wp-content/uploads/2014/02/Beaches-of-Cuba-Sunset.jpg';
    results["percent"] = '12';

    $scope.result = results;
    $scope.comp = false;
    $scope.won = true;

    $scope.game_submit = function(chosen) {
        if ((chosen).toString().valueOf() == ($scope.result["correct"]).valueOf()) {
            $scope.won = true;
            $log.log($scope.won);
        } else {
            $scope.won = false;
        }
        $scope.comp = true;
    }

    $log.log(results);
}]);
