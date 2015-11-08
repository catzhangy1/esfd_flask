angular.module('esfd', [
    'ngRoute',
    'esfd.home',
    'esfd.search',
    'esfd.results'])

.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      otherwise({
        redirectTo: '/home'
      });
  }]);
