@foreach($items as $item)
    <div>
        <p>
            {{$item['name']}}
            {{$item['price']}}
        </p>
        <img src="{{$item['image_urls']}}"/>
    </div>
@endforeach
