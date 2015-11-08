var esfd= angular.module('esfd', [
    'ngRoute'
]);

esfd.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/login', {
        templateUrl: '../templates/login.html',
        controller: 'loginCtrl'
      }).
        when('/home', {
          templateUrl: 'home.html',
          controller: 'homeCtrl'
        }).
      when('/success', {
        templateUrl: '../templates/login-success.html',
        controller: 'UserDetailCtrl'
      }).
      when('/matching', {
        templateUrl: '../tamplates/match.html',
        controller: 'MatchCtrl'
      }).
      otherwise({
        redirectTo: '/home'
      });
  }]);