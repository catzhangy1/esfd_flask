'use strict';

angular.module('esfd.search', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/search', {
            templateUrl: '../static/js/search.html',
            controller: 'SearchCtrl'
        });
    }])

    .controller('SearchCtrl', ['$scope','$log', '$window', '$http', function($scope, $log, $window, $http ) {
            $log.log("test");
            console.log('test');
            $http.get('/search',null).
                success(function(results){

                    results.map(function (o){$log.log(o)});
                    $log.log(results);
                    $window.location.path = ('/results');
                }).
                error(function(error){
                    $log.log(error);
                });

    }]);