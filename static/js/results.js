'use strict';

angular.module('esfd.results', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/results', {
            templateUrl: '../static/js/results.html',
            controller: 'ResultsCtrl'
        });
    }])


.controller('ResultsCtrl', ['$scope','$log', 'dataService', function($scope, $log, dataService) {
    $log.log('launched results');
    $log.log(dataService.getResult());
        var results = dataService.getResult();
        if(results.length == 1){
            $scope.result = results[0];
        } else{
            //do something else with multi list view
            $scope.result = results[0];
        }
        $log.log($scope.result);

}]);