$(function () {

    var $formAddBid = $('form[data-add-bid]');
    if ($formAddBid.length > 0) {
        var $minus = $formAddBid.find('[data-minus]'),
            $plus = $formAddBid.find('[data-plus]'),
            $input = $formAddBid.find('[name=bid]'),
            minValues = parseInt($input.data('min-value')),
            step = parseInt($input.data('step'));

        $minus.off('click').on('click', function (event) {
            event.preventDefault();
            var currentValue = parseInt($input.data('value')),
                newValue = currentValue - step;
            if (newValue >= minValues) {
                $input.data('value', newValue);
                $input.val(new Intl.NumberFormat('ru-RU').format(newValue));
            }
        });

        $plus.off('click').on('click', function (event) {
            event.preventDefault();
            var currentValue = parseInt($input.data('value')),
                newValue = currentValue + step;
            if (newValue >= minValues) {
                $input.data('value', newValue);
                $input.val(new Intl.NumberFormat('ru-RU').format(newValue));
            }
        });
    }

});