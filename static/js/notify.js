'use strict';

angular.module('esfd.notify', ['ngRoute'])

    .config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/notify', {
            templateUrl: '../static/js/notify.html',
            controller: 'NotifyCtrl'
        });
    }])

    .controller('NotifyCtrl',
    ['$scope','$log','$http',
        function($scope, $log, $http) {
            $scope.name = '';
            $scope.rEmail = '';
            $scope.sEmail = '';

            $scope.submit = function() {
                if($scope.name == '' && $scope.rEmail == '' && $scope.sEmail == ''){
                    return;
                }

                $log.log($scope.name);
                $log.log($scope.rEmail);
                $log.log($scope.sEmail);
                var data = [$scope.name, $scope.rEmail, $scope.sEmail];
                $log.log(data.join(" "));
                $http.post('/search', data, null).
                    success(function(results){
                        $log.log(results);
                    }).
                    error(function(error){
                        $log.log(error);
                    });
            }
        }
    ]);