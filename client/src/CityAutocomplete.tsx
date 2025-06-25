//client/src/CityAutocomplete.tsx

import React, { useRef } from 'react';

declare global {
  interface Window {
    google: any;
  }
}

const CityAutocomplete = ({ onSelect }: { onSelect: (city: string) => void }) => {
  const inputRef = useRef<HTMLInputElement>(null);

  React.useEffect(() => {
    if (!window.google) return;
    const autocomplete = new window.google.maps.places.Autocomplete(inputRef.current!, {
      types: ['(cities)'],
    });
    autocomplete.addListener('place_changed', () => {
      const place = autocomplete.getPlace();
      onSelect(place.name || '');
    });
  }, []);

  return <input ref={inputRef} placeholder="Enter your city" />;
};

export default CityAutocomplete;
