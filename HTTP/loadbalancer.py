from flask import Flask

loadbalancer = Flash(__name__)

@loadbalancer.route('/')
def router():
  return None
