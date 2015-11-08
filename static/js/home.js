'use strict';

angular.module('esfd.home', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/home', {
            templateUrl: '../static/js/home.html',
            controller: 'HomeCtrl'
        });
    }])

    .controller('HomeCtrl', ['$scope','$log', '$window', '$http', function($scope, $log, $window, $http ) {
        $log.log('launched');
        $scope.getResults = function (){
            $log.log("test");
            console.log('test');
            $http.get('/search',null).
                success(function(results){
                $log.log(results);
                    $window.location.path = ('/results');
            }).
            error(function(error){
                $log.log(error);
            });
        };
    }]);