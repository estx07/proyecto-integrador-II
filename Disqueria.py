import consulta
import cargadatos


def main():
    
    #Primera Lista
    busqueda = consulta.ListarAlbums()
    busqueda.PorGenero("Instrumental")

    busqueda.PorArtista("Michael","Jackson")

    Listar1 = consulta.ListarInterpretes()
    Listar1.ListaCompleta

    carga = cargadatos.Cargar()
    carga.CargarInterprete("Phil","Collins","UK","https://www.discos.com/lafotodelartista.jpg")
    














if __name__ == '__main__':
    main()