import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import { Button } from 'primereact/button'; 
import "primereact/resources/themes/saga-blue/theme.css";

export default function MyApp({ Component, pageProps }) {
    return (
        <PrimeReactProvider>
            <Component {...pageProps} />
        </PrimeReactProvider>
    );
}