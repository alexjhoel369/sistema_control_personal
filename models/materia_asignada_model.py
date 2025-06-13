from database import db

class Materia_asignada(db.Model):
    __tablename__ = "materias_asignadas"

    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    materia_id = db.Column(db.Integer, db.ForeignKey('materias.id'), nullable=False)
    gestion = db.Column(db.String(20), nullable=True)

    empleado = db.relationship('Empleado', back_populates='materias_asignadas')
    materia = db.relationship('Materia', back_populates='materias_asignadas')

    def __init__(self, empleado_id, materia_id, gestion):
        self.empleado_id = empleado_id
        self.materia_id = materia_id
        self.gestion = gestion

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Materia_asignada.query.all()

    @staticmethod
    def get_by_id(id):
        return Materia_asignada.query.get(id)

    def update(self, empleado_id=None, materia_id=None, gestion=None):
        if empleado_id:
            self.empleado_id = empleado_id
        if materia_id:
            self.materia_id = materia_id
        if gestion:
            self.gestion = gestion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
