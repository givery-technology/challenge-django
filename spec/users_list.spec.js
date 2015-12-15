"use strict";
var
  assert = require("chai").assert,
  spec = require("api-first-spec");

var API = spec.define({
  "endpoint": "/api/users/",
  "method": "GET",
  "request": {
    "contentType": spec.ContentType.URLENCODED,
  },
  "response": {
    "contentType": spec.ContentType.JSON,
    "data": {
      "user": [{
        "id": "int",
        "username": "string",
        "email": "string",
        "birthday": "date",
        "company": "string",
        "location": "string"
      }]
    }
  }
});

describe("login", function() {
  var host = spec.host("localhost:8000");

  it("Testing", function(done) {
    host.api(API).success(function(data) {
      // console.log(data);
      assert.equal(data[0].username, "user1");
      done();
    });
  });
});

module.exports = API;