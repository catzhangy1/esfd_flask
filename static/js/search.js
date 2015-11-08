'use strict';

angular.module('esfd.search', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/search', {
            templateUrl: '../static/js/search.html',
            controller: 'SearchCtrl'
        });
    }])

    .controller('SearchCtrl', [function() {

    }]);