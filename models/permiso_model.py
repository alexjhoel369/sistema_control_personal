from database import db
from datetime import date

class Permiso(db.Model):
    __tablename__ = "permisos"

    id = db.Column(db.Integer, primary_key=True)
    fecha_solicitud = db.Column(db.Date, default=date.today, nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    motivo = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(20), nullable=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)

    empleado = db.relationship('Empleado', back_populates='permisos')

    def __init__(self, fecha_solicitud, fecha_inicio, fecha_fin, motivo, estado, empleado_id):
        self.fecha_solicitud = fecha_solicitud
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.motivo = motivo
        self.estado = estado
        self.empleado_id = empleado_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Permiso.query.all()

    @staticmethod
    def get_by_id(id):
        return Permiso.query.get(id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
