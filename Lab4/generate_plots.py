
system = MassSpringDamper(1.0, 5.0, 2.5)
state, times = system.simulate(1, -1, 40, 0.01)
