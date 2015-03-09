from sqlalchemy.dialects import registry

registry.register("vtgatev3", "sqlalchemy_vtgatev3.vtgatev3", "VTGatev3Dialect")
