'use strict';

angular.module('esfd.results', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/results', {
            templateUrl: '../static/js/results.html',
            controller: 'ResultsCtrl'
        });
    }])

    .controller('ResultsCtrl', [function() {

    }]);