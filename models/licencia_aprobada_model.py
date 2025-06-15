from database import db
from sqlalchemy.orm import joinedload 

class LicenciaAprobada(db.Model):
    __tablename__ = "licencias_aprobadas"

    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    tipo_licencia_id = db.Column(db.Integer, db.ForeignKey('tipos_licencia.id'), nullable=False)
    gestion = db.Column(db.String(20), nullable=True)

    empleado = db.relationship('Empleado', back_populates='licencias_aprobadas')
    tipo_licencia = db.relationship('TipoLicencia', back_populates='licencias_aprobadas')

    def __init__(self, empleado_id, tipo_licencia_id, gestion):
        self.empleado_id = empleado_id
        self.tipo_licencia_id = tipo_licencia_id
        self.gestion = gestion

    def save(self):
        db.session.add(self)
        db.session.commit()


    @staticmethod
    def get_all():
        return LicenciaAprobada.query.options(
            joinedload(LicenciaAprobada.empleado),
            joinedload(LicenciaAprobada.tipo_licencia)
            ).all()


    @staticmethod
    def get_by_id(id):
        return LicenciaAprobada.query.get(id)

    def update(self, empleado_id=None, tipo_licencia_id=None, gestion=None):
        if empleado_id:
            self.empleado_id = empleado_id
        if tipo_licencia_id:
            self.tipo_licencia_id = tipo_licencia_id
        if gestion:
            self.gestion = gestion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
