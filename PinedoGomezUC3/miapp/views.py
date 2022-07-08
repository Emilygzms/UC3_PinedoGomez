from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    mensaje="""
        <h1>Universidad Nacional Tecnológica de Lima Sur</h1>
        <h2>EP Ingeniería de Sistemas</h2>
        <h3>Bienvenidos :D</h3>
    """
    return HttpResponse(mensaje)

def uc3(request):
    mensaje="""
        <h1>Lenguaje de Programación III</h1>
        <h2>Evaluación de la Unidad de Competencia 3</h2>
        <h2>Docente: Mg. Flor Elizabeth Cerdán León</h2>
        <h3>Integrantes: </h3>
        <li>Estudiante 1</li>
        <li>Estudiante 2</li>
        <li>Estudiante 3</li>
    """
    return HttpResponse(mensaje)

def noticia(request):
    mensaje="""
        <h1>Con Advíncula y Zambrano: Boca Juniors anunció a los convocados para el partido ante San Lorenzo</h1>
        <h2>El ‘Xeneize’ deberá voltear la página de la eliminación de la Copa Libertadores 2022 y, ahora, se enfocará en recuperarse el paso en el torneo local.</h2>
        <p>Boca Juniors tuvo una semana complicada por la eliminación de la Copa Libertadores a manos de Corinthians y también se quedó sin entrenador tras la salida de Sebastián Battaglia. Sin embargo, el ‘Xeneize’ se debe mentalizar en el encuentro de visita ante San Lorenzo por la Liga Profesional de Argentina.
        En ese sentido, la ‘Azul y Oro’, que será dirigida de manera interna por Hugo Ibarra, anunció a los convocados para el compromiso contra el ‘Ciclón’ que se jugará este sábado a partir de la 1:30 p. m. (hora peruana). Al respecto, Luis Advíncula y Carlos Zambrano figuran en la lista de nominados.</p>
        <img src="https://elcomercio.pe/resizer/NPDfIHEAMOt2xMymyc8yykjR7B0=/580x330/smart/filters:format(jpeg):quality(75)/cloudfront-us-east-1.images.arcpublishing.com/elcomercio/7IN5LGYZTNFMLLCHKFHCB3RUHM.jpg">
    """
    return HttpResponse(mensaje)