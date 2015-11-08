'use strict';

angular.module('esfd.admin', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/admin', {
            templateUrl: '../static/js/admin.html',
            controller: 'AdminCtrl'
        });
    }])

    .controller('AdminCtrl',
    ['$scope','$log','$http',
        function($scope, $log, $http) {
            $scope.origin = '';
            $scope.dest = '';
            $scope.hotel = '';
            $scope.date = '';
            $scope.nights = 0;
            $scope.checkin = '';
            $scope.checkout = '';
            $scope.expedia = 0;
            $scope.jetblue = 0;
            $scope.percent = 0;
            $scope.month = 0;
            $scope.weeks = 0;

            $scope.submit = function() {

                var data = [$scope.origin,
                $scope.dest,
                $scope.hotel,
                $scope.nights,
                $scope.checkin,
                $scope.checkout,
                $scope.expedia,
                $scope.jetblue,
                $scope.percent,
                $scope.month,
                $scope.weeks];

                $log.log(data);
                $http({method: "POST", url:"/admin", data:data}).
                    success(function(results){
                        $log.log(results);
                    }).
                    error(function(error){
                        $log.log(error);
                    });
            }
        }
    ]);